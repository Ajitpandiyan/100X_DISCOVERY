import pytest
import streamlit as st
from src.config import BACKEND_API_KEY, STREAMLIT_TOKEN, Settings, settings


def test_api_keys():
    """Test if API keys are properly loaded"""
    print("\n=== API Keys Loading Test ===")

    # Test Streamlit Token
    print("\n1. Testing Streamlit Token:")
    if STREAMLIT_TOKEN:
        print("✅ Streamlit Token is loaded")
        print(f"   Length: {len(STREAMLIT_TOKEN)} characters")
        print(f"   First 10 chars: {STREAMLIT_TOKEN[:10]}...")
    else:
        print("❌ Streamlit Token not found!")

    # Test Backend API Key
    print("\n2. Testing Backend API Key:")
    if BACKEND_API_KEY:
        print("✅ Backend API Key is loaded")
        print(f"   Length: {len(BACKEND_API_KEY)} characters")
        print(f"   First 10 chars: {BACKEND_API_KEY[:10]}...")
    else:
        print("❌ Backend API Key not found!")

    # Test Settings
    print("\n3. Testing Settings Configuration:")
    print(f"✅ Backend URL: {settings.BACKEND_API_URL}")
    print(
        f"✅ Backend API Key from settings: {'Present' if settings.BACKEND_API_KEY else 'Missing'}"
    )


def test_settings():
    """Test that settings can be loaded"""
    settings = Settings()
    assert settings is not None
    assert hasattr(settings, "backend_api_url")
    assert hasattr(settings, "backend_api_key")


if __name__ == "__main__":
    test_api_keys()
