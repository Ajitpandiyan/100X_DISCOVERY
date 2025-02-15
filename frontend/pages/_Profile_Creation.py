import streamlit as st

from src.components.profile_form import render_profile_form

st.set_page_config(
    page_title="Create Profile - 100X Discovery", page_icon="👤", layout="wide"
)


def main():
    st.header("Create Your Profile")
    st.markdown("---")

    render_profile_form()


if __name__ == "__main__":
    main()
