# backend/app/core/security.py

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import re
import os

# --- LOAD FROM ENV ---
SECRET_KEY = os.getenv("SECRET_KEY", "SuperSecretKeyOmniCalc")  # default fallback
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
FRONTEND_DOMAIN = os.getenv("FRONTEND_DOMAIN", "https://nazumiizuma-dot.github.io")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security_scheme = HTTPBearer()

# --- JWT FUNCTIONS ---
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication token")

# --- PASSWORD HASHING ---
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# --- AUTH DEPENDENCY ---
def get_current_user(credentials: HTTPAuthorizationCredentials = security_scheme):
    token = credentials.credentials
    return verify_access_token(token)

# --- RATE LIMIT & SANITIZATION ---
def sanitize_input(user_input: str) -> str:
    sanitized = re.sub(r"[<>\"'%;()&+]", "", user_input)
    return sanitized.strip()

# --- CORS & SECURITY HEADERS (FastAPI middleware) ---
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_security_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[FRONTEND_DOMAIN],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.middleware("http")
    async def add_headers(request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
        return response

# --- SAMPLE USAGE: default user password ---
def default_user_password():
    return hash_password("Lvy12345")
