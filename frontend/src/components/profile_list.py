import streamlit as st

from ..utils.api import APIClient


def display_profile_card(profile):
    """Display a single profile in a card format"""
    # Get profile fields with default values for missing fields
    name = profile.get('name', 'Unknown Name')
    bio = profile.get('bio', 'No bio provided')
    skills = profile.get('skills', [])
    interests = profile.get('interests', [])
    experience_level = profile.get('experience_level', 'Not specified')

    # Format skills and interests as comma-separated strings
    skills_str = ', '.join(skills) if skills else 'None specified'
    interests_str = ', '.join(interests) if interests else 'None specified'

    with st.container():
        st.markdown(
            f"""
            <div class="profile-card">
                <h3>{name}</h3>
                <p><strong>Bio:</strong> {bio}</p>
                <p><strong>Skills:</strong> {skills_str}</p>
                <p><strong>Interests:</strong> {interests_str}</p>
                <p><strong>Experience Level:</strong> {experience_level}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_profile_list():
    """Display all profiles"""
    st.title("All Profiles")

    api_client = APIClient()

    # Add refresh button
    if st.button("🔄 Refresh Profiles"):
        st.cache_data.clear()
        st.rerun()

    # Debug information
    st.write(f"Debug - Backend URL: {api_client.base_url}")

    with st.spinner("Loading profiles..."):
        result = api_client.get_all_profiles()

    # Debug the raw API response
    with st.expander("Debug - API Response"):
        st.json(result)

    if "profiles" not in result or not result["profiles"]:
        st.warning(
            "No profiles found. Create some profiles using the Profile Creation tab!"
        )

        # Add a sample profile creation button for testing
        if st.button("Create Sample Profile for Testing"):
            sample_profile = {
                "name": "Sample User",
                "bio": "This is a sample profile for testing purposes.",
                "skills": ["Python", "React", "FastAPI"],
                "interests": ["Machine Learning", "Web Development"],
                "experience_level": "Intermediate",
            }
            create_result = api_client.create_profile(sample_profile)
            st.write("Sample profile creation result:", create_result)
            st.cache_data.clear()
            st.rerun()
        return

    profiles = result["profiles"]
    st.success(f"Found {len(profiles)} profiles")

    # Add sorting options
    sort_by = st.selectbox("Sort by", ["Name", "Experience Level"], key="profile_sort")

    if sort_by == "Name":
        profiles.sort(key=lambda x: x.get("name", "").lower())
    elif sort_by == "Experience Level":
        level_order = {"Beginner": 1, "Intermediate": 2, "Advanced": 3, "Expert": 4}
        profiles.sort(key=lambda x: level_order.get(x.get("experience_level", ""), 0))

    # Add search/filter
    search_term = st.text_input(
        "Filter profiles", placeholder="Type to filter by name, skills, or interests"
    )
    if search_term:
        search_term = search_term.lower()
        filtered_profiles = []
        for p in profiles:
            # Get profile fields with default values
            name = p.get('name', '').lower()
            skills = [s.lower() for s in p.get('skills', [])]
            interests = [i.lower() for i in p.get('interests', [])]
            bio = p.get('bio', '').lower()

            # Check if search term is in any of the fields
            if (
                search_term in name
                or search_term in bio
                or any(search_term in skill for skill in skills)
                or any(search_term in interest for interest in interests)
            ):
                filtered_profiles.append(p)
        profiles = filtered_profiles

    # Display profiles in a grid
    if profiles:
        cols = st.columns(2)
        for idx, profile in enumerate(profiles):
            with cols[idx % 2]:
                display_profile_card(profile)
    else:
        st.warning("No profiles match your filter criteria.")
