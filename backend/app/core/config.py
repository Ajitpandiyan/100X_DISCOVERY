from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost:8501"]
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()