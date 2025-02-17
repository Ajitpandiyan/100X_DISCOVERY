"""Configuration module for the frontend application."""

import os
import streamlit as st
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings."""

    backend_api_url: str = os.getenv("BACKEND_API_URL", "http://localhost:8000")
    backend_api_key: str = os.getenv("BACKEND_API_KEY", "")
    streamlit_token: str = os.getenv("STREAMLIT_TOKEN", "")

    class Config:
        """Pydantic configuration."""
        env_file = ".env"


def get_streamlit_token() -> str | None:
    """
    Get Streamlit API token from environment variables or secrets.

    Returns:
        str | None: Token in order of precedence:
            1. Environment variable
            2. Streamlit secrets
            3. None
    """
    # First try environment variable
    token = os.getenv("STREAMLIT_TOKEN")

    # Then try streamlit secrets
    if not token and "streamlit_token" in st.secrets:
        token = st.secrets["streamlit_token"]

    return token


def get_backend_api_key() -> str | None:
    """
    Get Backend API key from environment variables or secrets.

    Returns:
        str | None: Key in order of precedence:
            1. Environment variable
            2. Streamlit secrets
            3. None
    """
    # First try environment variable
    key = os.getenv("BACKEND_API_KEY")

    # Then try streamlit secrets
    if not key and "backend_api_key" in st.secrets:
        key = st.secrets["backend_api_key"]

    return key


# Initialize settings
settings = Settings()

# Export commonly used settings
BACKEND_API_URL = settings.backend_api_url
BACKEND_API_KEY = settings.backend_api_key
STREAMLIT_TOKEN = settings.streamlit_token
