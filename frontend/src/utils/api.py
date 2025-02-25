import httpx
import streamlit as st
import time
from httpx import ConnectError, ReadTimeout, HTTPStatusError

from ..config import BACKEND_API_KEY, settings


class APIClient:
    def __init__(self):
        self.base_url = settings.backend_api_url
        self.headers = {
            "Authorization": f"Bearer {BACKEND_API_KEY}",
            "Content-Type": "application/json",
        }
        self.timeout = 10.0  # 10 seconds timeout

    @st.cache_data(ttl=300)
    def create_profile(_self, profile_data):
        """Create a new profile"""
        try:
            response = httpx.post(
                f"{_self.base_url}/api/v1/profiles/",
                json=profile_data,
                headers=_self.headers,
                timeout=_self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except ConnectError:
            st.error(f"Could not connect to backend server at {_self.base_url}. Please check if the server is running.")
            return {"error": "Connection error"}
        except ReadTimeout:
            st.error("Request timed out. The backend server might be overloaded.")
            return {"error": "Timeout error"}
        except HTTPStatusError as e:
            st.error(f"Server error: {e.response.status_code} - {e.response.text}")
            return {"error": f"HTTP error: {e.response.status_code}"}
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
            return {"error": "Unexpected error"}

    @st.cache_data(ttl=300)
    def search_profiles(_self, query):
        """Search for profiles"""
        try:
            response = httpx.get(
                f"{_self.base_url}/api/v1/search/",
                params={"query": query},
                headers=_self.headers,
                timeout=_self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except ConnectError:
            st.error(f"Could not connect to backend server at {_self.base_url}. Please check if the server is running.")
            return {"matches": []}
        except ReadTimeout:
            st.error("Search request timed out. The backend server might be overloaded.")
            return {"matches": []}
        except HTTPStatusError as e:
            st.error(f"Server error: {e.response.status_code} - {e.response.text}")
            return {"matches": []}
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
            return {"matches": []}
