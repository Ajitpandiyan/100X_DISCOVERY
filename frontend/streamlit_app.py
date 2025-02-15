import streamlit as st

from src.components.profile_form import render_profile_form
from src.components.search_interface import render_search_interface
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
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #eee;
        margin: 1rem 0;
        background-color: #F0F2F6;
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
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #333;
        margin: 1rem 0;
        background-color: #1E2127;
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
    st.title("100X Discovery Platform v1.0")
    st.caption("Connect with talented engineers and discover opportunities")

    # Theme toggle in sidebar
    with st.sidebar:
        if st.button("🌓 Toggle Theme"):
            st.session_state.theme = (
                "dark" if st.session_state.theme == "light" else "light"
            )
            st.rerun()

    # Main navigation
    tab1, tab2 = st.tabs(["Profile Creation", "Search"])

    with tab1:
        render_profile_form()

    with tab2:
        render_search_interface()


if __name__ == "__main__":
    main()
