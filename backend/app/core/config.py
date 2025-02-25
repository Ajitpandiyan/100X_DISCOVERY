"""Application configuration module."""

from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    # API Configuration
    ENVIRONMENT: str = "development"
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:8501", "http://localhost:8502"]
    
    # External Services
    GROQ_API_KEY: str = ""

    class Config:
        """Pydantic configuration."""
        
        case_sensitive = True
        env_file = ".env"


settings = Settings()