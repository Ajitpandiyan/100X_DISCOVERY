import streamlit as st
from typing import Optional
import os
from services.api_service import APIService
from components.profile_form import profile_form
from components.search_box import search_box
from utils.cache import cache_api_response

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

# Sidebar navigation
def sidebar():
    st.sidebar.title("Navigation")
    return st.sidebar.radio(
        "Go to",
        ["Home", "Create Profile", "Search Profiles"]
    )

# Home page
def home():
    st.title("100X Discovery Platform")
    
    st.markdown("""
    Welcome to the 100X Discovery Platform! This platform helps connect talented engineers 
    with exciting opportunities.
    
    ### Features:
    - Create and manage your professional profile
    - Search for other engineers based on skills and experience
    - Connect with fellow 100X Engineers
    """)
    
    # Display platform stats
    try:
        profiles = api_service.get_all_profiles()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Profiles", len(profiles))
        with col2:
            unique_skills = set()
            for profile in profiles:
                unique_skills.update(profile['skills'])
            st.metric("Unique Skills", len(unique_skills))
    except Exception as e:
        st.error("Error loading platform statistics")

# Create Profile page
def create_profile():
    st.title("Create Your Profile")
    
    st.markdown("""
    Fill in the form below to create your profile. This information will be used to help others discover you 
    and your skills. Fields marked with * are required.
    """)
    
    profile_form(api_service)

# Search page
def search_profiles():
    st.title("Search Profiles")
    
    st.markdown("""
    Search for other engineers based on skills, experience, or any other criteria. 
    The search uses AI to find the most relevant matches for your query.
    """)
    
    search_box(api_service)
    
    with st.expander("Search Tips"):
        st.markdown("""
        Here are some effective ways to search:
        - Search by specific skills: "Python developer with React experience"
        - Search by role: "Full stack developer"
        - Search by domain: "Machine learning engineer interested in NLP"
        - Search by experience level: "Senior backend developer"
        """)

def main():
    # Navigation
    page = sidebar()
    
    # Page routing
    if page == "Home":
        home()
    elif page == "Create Profile":
        create_profile()
    elif page == "Search Profiles":
        search_profiles()

if __name__ == "__main__":
    main() 
