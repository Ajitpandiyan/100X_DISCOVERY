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

    # Backend API Keys
    BACKEND_API_KEY: str = (
        "f31gui6pzr9v6y1o3j29ab9jdfj48jcncmhw1emzru14aiamotla90i2e4um2owx"
    )
    BACKEND_API_URL: str = "http://localhost:8000"

    class Config:
        """Pydantic configuration."""

        case_sensitive = True
        env_file = ".env"
        # Allow extra fields from environment variables
        extra = "ignore"


settings = Settings()
