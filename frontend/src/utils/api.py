import httpx
from ..config import settings, BACKEND_API_KEY
import streamlit as st

class APIClient:
    def __init__(self):
        self.base_url = settings.BACKEND_API_URL
        self.headers = {
            "Authorization": f"Bearer {BACKEND_API_KEY}",
            "Content-Type": "application/json"
        }
    
    @st.cache_data(ttl=300)
    def create_profile(_self, profile_data):
        """Create a new profile"""
        response = httpx.post(
            f"{_self.base_url}/api/v1/profiles/",
            json=profile_data,
            headers=_self.headers
        )
        response.raise_for_status()
        return response.json()
    
    @st.cache_data(ttl=300)
    def search_profiles(_self, query):
        """Search for profiles"""
        response = httpx.get(
            f"{_self.base_url}/api/v1/search/",
            params={"query": query},
            headers=_self.headers
        )
        response.raise_for_status()
        return response.json()