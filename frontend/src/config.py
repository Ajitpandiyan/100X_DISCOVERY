"""Configuration module for the frontend application."""

import os
from typing import Optional

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
    groq_api_key: str = os.getenv("GROQ_API_KEY", "")

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        # Allow case-insensitive environment variables
        env_nested_delimiter = "__"
        case_sensitive = False
        # Allow extra fields to avoid validation errors
        extra = "ignore"


def get_streamlit_token() -> Optional[str]:
    """
    Get Streamlit API token from environment variables or secrets.

    Returns:
        Optional[str]: Token in order of precedence:
            1. Environment variable
            2. Streamlit secrets
            3. None
    """
    # First try environment variable
    token = os.getenv("STREAMLIT_TOKEN")

    # Then try streamlit secrets
    if not token and "streamlit_token" in st.secrets["general"]:
        token = st.secrets["general"]["streamlit_token"]

    return token


def get_backend_api_key() -> Optional[str]:
    """
    Get Backend API key from environment variables or secrets.

    Returns:
        Optional[str]: Key in order of precedence:
            1. Environment variable
            2. Streamlit secrets
            3. None
    """
    # First try environment variable
    key = os.getenv("BACKEND_API_KEY")

    # Then try streamlit secrets
    if not key and "backend_api_key" in st.secrets["general"]:
        key = st.secrets["general"]["backend_api_key"]

    return key


def get_groq_api_key() -> Optional[str]:
    """
    Get GROQ API key from environment variables or secrets.
    
    Returns:
        Optional[str]: Key in order of precedence:
            1. Environment variable
            2. Streamlit secrets
            3. None
    """
    # First try environment variable
    key = os.getenv("GROQ_API_KEY")
    
    # Then try streamlit secrets
    if not key and "groq_api_key" in st.secrets["general"]:
        key = st.secrets["general"]["groq_api_key"]
        
    return key


# Initialize settings
settings = Settings()

# Export commonly used settings
BACKEND_API_URL = settings.backend_api_url
BACKEND_API_KEY = settings.backend_api_key
STREAMLIT_TOKEN = settings.streamlit_token
GROQ_API_KEY = settings.groq_api_key
