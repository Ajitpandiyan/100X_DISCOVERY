import streamlit as st
from src.components.search_interface import run_search

st.set_page_config(
    page_title="Search - 100X Discovery",
    page_icon="🔍",
    layout="wide",
)

# Run the search interface
run_search()


def main():
    st.header("Search Profiles")
    st.markdown("---")

    render_search_interface()


if __name__ == "__main__":
    main()
