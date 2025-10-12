from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import calculators
from app.core.config import settings
from prometheus_client import start_http_server

app = FastAPI(title="OmniCalc Pro API", version="1.0.0", docs_url="/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calculators.router, prefix="/api/v1/calculators", tags=["calculators"])

@app.get("/health")
async def health():
    return {"status": "ok"}

try:
    start_http_server(settings.PROMETHEUS_PORT)
except Exception:
    pass
