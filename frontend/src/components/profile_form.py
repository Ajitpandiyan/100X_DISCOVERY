import streamlit as st

from ..utils.api import APIClient


def render_profile_form():
    st.header("Create Your Profile")

    with st.form("profile_form"):
        name = st.text_input("Full Name*", placeholder="John Doe")
        bio = st.text_area("Bio*", placeholder="Tell us about yourself...")

        col1, col2 = st.columns(2)
        with col1:
            skills = st.multiselect(
                "Skills*",
                options=[
                    "Python",
                    "JavaScript",
                    "React",
                    "Node.js",
                    "Machine Learning",
                    "Data Science",
                    "FastAPI",
                    "DevOps",
                ],
                default=None,
            )
        with col2:
            interests = st.multiselect(
                "Interests*",
                options=[
                    "Web Development",
                    "AI/ML",
                    "Mobile Development",
                    "Cloud Computing",
                    "Blockchain",
                    "IoT",
                ],
                default=None,
            )

        github_url = st.text_input(
            "GitHub Profile URL", placeholder="https://github.com/yourusername"
        )
        linkedin_url = st.text_input(
            "LinkedIn Profile URL", placeholder="https://linkedin.com/in/yourusername"
        )

        submitted = st.form_submit_button("Create Profile")

        if submitted:
            if not name or not bio or not skills or not interests:
                st.error("Name, bio, skills, and interests are required!")
                return

            profile_data = {
                "name": name,
                "bio": bio,
                "skills": skills,
                "interests": interests,
                "github_url": github_url if github_url else None,
                "linkedin_url": linkedin_url if linkedin_url else None,
            }

            try:
                client = APIClient()
                response = client.create_profile(profile_data)
                st.success("Profile created successfully!")
                st.json(response)
            except Exception as e:
                st.error(f"Error creating profile: {str(e)}")
