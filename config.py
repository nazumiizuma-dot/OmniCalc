from pydantic import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "OmniCalc Pro"
    CORS_ORIGINS: List[str] = ["http://localhost:3000","http://localhost:3001"]
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/omnicalc"
    REDIS_URL: str = "redis://redis:6379/0"
    JWT_SECRET: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    SANDBOX_TIMEOUT: int = 3
    PROMETHEUS_PORT: int = 8001
    OPENAI_API_KEY: str | None = None
    class Config:
        env_file = ".env"

settings = Settings()
