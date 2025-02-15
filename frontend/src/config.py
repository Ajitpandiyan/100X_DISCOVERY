from pydantic_settings import BaseSettings
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    BACKEND_API_URL: str = "http://localhost:8000"
    BACKEND_API_KEY: str = ""
    STREAMLIT_TOKEN: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True

def get_streamlit_token():
    """
    Get Streamlit API token from environment variables or secrets
    Returns in order of precedence:
    1. Environment variable
    2. Streamlit secrets
    3. None
    """
    # First try environment variable
    token = os.getenv("STREAMLIT_TOKEN")
    
    # Then try streamlit secrets
    if not token and 'streamlit_token' in st.secrets:
        token = st.secrets['streamlit_token']
        
    return token

def get_backend_api_key():
    """
    Get Backend API key from environment variables or secrets
    Returns in order of precedence:
    1. Environment variable
    2. Streamlit secrets
    3. None
    """
    # First try environment variable
    key = os.getenv("BACKEND_API_KEY")
    
    # Then try streamlit secrets
    if not key and 'backend_api_key' in st.secrets:
        key = st.secrets['backend_api_key']
        
    return key

# Export the tokens for use in other files
STREAMLIT_TOKEN = get_streamlit_token()
BACKEND_API_KEY = get_backend_api_key()

settings = Settings()