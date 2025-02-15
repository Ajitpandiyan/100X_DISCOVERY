import streamlit as st
from src.components.search_interface import render_search_interface

st.set_page_config(
    page_title="Search - 100X Discovery",
    page_icon="🔍",
    layout="wide"
)

def main():
    st.header("Search Profiles")
    st.markdown("---")
    
    render_search_interface()

if __name__ == "__main__":
    main()