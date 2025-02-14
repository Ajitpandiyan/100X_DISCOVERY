import streamlit as st
from typing import Optional
import os

# Use relative imports
from .services.api_service import APIService
from .components.profile_form import profile_form
from .components.search_box import search_box
from .utils.cache import cache_api_response

# Initialize services
api_service = APIService()

# Page configuration
st.set_page_config(
    page_title="100X Discovery Platform",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("100X Discovery Platform")
    st.markdown("""
    Welcome to the 100X Discovery Platform! This platform helps connect talented engineers 
    with exciting opportunities.
    """)

if __name__ == "__main__":
    main()
