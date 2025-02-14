import streamlit as st
from typing import Optional
import os
# Fix the imports by adding src.
from src.services.api_service import APIService
from src.components.profile_form import profile_form
from src.components.search_box import search_box
from src.utils.cache import cache_api_response

# Initialize services
api_service = APIService()

# Page configuration
st.set_page_config(
    page_title="100X Discovery Platform",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .profile-card {
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #eee;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("100X Discovery Platform")
    
    st.markdown("""
    Welcome to the 100X Discovery Platform! This platform helps connect talented engineers 
    with exciting opportunities.
    
    ### Features:
    - Create and manage your professional profile
    - Search for other engineers based on skills and experience
    - Connect with fellow 100X Engineers
    """)

if __name__ == "__main__":
    main()
