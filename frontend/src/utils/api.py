import time

import httpx
import streamlit as st
from httpx import ConnectError, HTTPStatusError, ReadTimeout

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
            st.error(
                f"Could not connect to backend server at {_self.base_url}. Please check if the server is running."
            )
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
            # Increase timeout for semantic search which can take longer
            search_timeout = 30.0  # 30 seconds timeout for search

            st.info(
                "Searching for profiles... This may take a few seconds for semantic search."
            )

            # Add timestamp to avoid caching issues
            timestamp = int(time.time())

            # Ensure the URL is correctly formed with no trailing slash
            search_url = f"{_self.base_url.rstrip('/')}/api/v1/search?t={timestamp}"
            st.write(f"Debug - Search URL: {search_url}")

            response = httpx.post(
                search_url,
                json={"query": query},
                headers=_self.headers,
                timeout=search_timeout,
                follow_redirects=True,  # Add this to follow any redirects automatically
            )
            response.raise_for_status()
            result = response.json()

            if "matches" not in result:
                st.error("Invalid response format from the search API")
                return {"matches": []}

            return result
        except ConnectError:
            st.error(
                f"Could not connect to backend server at {_self.base_url}. Please check if the server is running."
            )
            return {"matches": []}
        except ReadTimeout:
            st.error(
                "Search request timed out. Semantic search can take longer when processing natural language queries."
            )
            return {"matches": []}
        except HTTPStatusError as e:
            st.error(f"Server error: {e.response.status_code} - {e.response.text}")
            return {"matches": []}
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
            return {"matches": []}

    @st.cache_data(ttl=60)  # Cache for 1 minute
    def get_all_profiles(_self):
        """Get all profiles"""
        try:
            # Ensure the URL is correctly formed with no trailing slash
            profiles_url = f"{_self.base_url.rstrip('/')}/api/v1/profiles/"
            st.write(f"Debug - Profiles URL: {profiles_url}")

            response = httpx.get(
                profiles_url,
                headers=_self.headers,
                timeout=_self.timeout,
            )

            # Debug response status
            st.write(f"Debug - Response status: {response.status_code}")

            response.raise_for_status()
            result = response.json()

            # If the response doesn't have a 'profiles' key, try to adapt the format
            if "profiles" not in result:
                # Check if the response is a list of profiles
                if isinstance(result, list):
                    return {"profiles": result}
                else:
                    st.error("Invalid response format from the profiles API")
                    return {"profiles": []}

            return result
        except ConnectError:
            st.error(
                f"Could not connect to backend server at {_self.base_url}. Please check if the server is running."
            )
            return {"profiles": []}
        except ReadTimeout:
            st.error("Request timed out. The backend server might be overloaded.")
            return {"profiles": []}
        except HTTPStatusError as e:
            st.error(f"Server error: {e.response.status_code} - {e.response.text}")
            return {"profiles": []}
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
            return {"profiles": []}
