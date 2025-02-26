import streamlit as st
from src.components.profile_form import render_profile_form
from src.components.profile_list import render_profile_list
from src.components.search_interface import run_search
from src.utils.api import APIClient

# Initialize session state for theme
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Custom CSS for themes
light_theme = """
<style>
    .main {
        background-color: #FFFFFF;
        color: #262730;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .profile-card {
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #eee;
        margin: 1rem 0;
        background-color: #F0F2F6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }
    .profile-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .profile-card h3 {
        color: #FF4B4B;
        margin-bottom: 1rem;
    }
    .profile-card p {
        margin: 0.5rem 0;
    }
</style>
"""

dark_theme = """
<style>
    .main {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .profile-card {
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #333;
        margin: 1rem 0;
        background-color: #1E2127;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        transition: transform 0.2s ease;
    }
    .profile-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .profile-card h3 {
        color: #FF4B4B;
        margin-bottom: 1rem;
    }
    .profile-card p {
        margin: 0.5rem 0;
    }
</style>
"""

st.set_page_config(
    page_title="100X Discovery",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def main():
    # Apply theme
    if st.session_state.theme == "light":
        st.markdown(light_theme, unsafe_allow_html=True)
    else:
        st.markdown(dark_theme, unsafe_allow_html=True)

    # Header
    st.title("100X Discovery Platform")
    st.caption("Connect with talented engineers and discover opportunities")

    # Theme toggle in sidebar
    with st.sidebar:
        if st.button("🌓 Toggle Theme"):
            st.session_state.theme = (
                "dark" if st.session_state.theme == "light" else "light"
            )
            st.rerun()

    # Main navigation
    tab1, tab2, tab3 = st.tabs(["Profile Creation", "All Profiles", "Search"])

    with tab1:
        render_profile_form()

    with tab2:
        render_profile_list()

    with tab3:
        run_search()


if __name__ == "__main__":
    main()
