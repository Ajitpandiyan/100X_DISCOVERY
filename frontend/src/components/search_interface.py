import streamlit as st

from ..utils.api import APIClient


def render_search_interface():
    st.header("Search Profiles")

    # Search input
    query = st.text_input(
        "Search by skills, interests, or keywords",
        placeholder="e.g., Python developer with ML experience",
    )

    if query:
        try:
            client = APIClient()
            results = client.search_profiles(query)

            if not results or len(results.get("matches", [])) == 0:
                st.info("No profiles found matching your search criteria.")
                return

            # Display results
            for profile in results.get("matches", []):
                with st.container():
                    col1, col2 = st.columns([2, 1])

                    with col1:
                        st.subheader(profile["name"])
                        st.write(profile["bio"])
                        if "score" in profile:
                            st.caption(f"Match Score: {profile['score']:.2f}")

                    with col2:
                        st.write("Skills:")
                        for skill in profile["skills"]:
                            st.write(f"- {skill}")

                        st.write("Interests:")
                        for interest in profile["interests"]:
                            st.write(f"- {interest}")

                    if profile.get("github_url") or profile.get("linkedin_url"):
                        st.write("Links:")
                        cols = st.columns(2)
                        if profile.get("github_url"):
                            cols[0].link_button("GitHub", profile["github_url"])
                        if profile.get("linkedin_url"):
                            cols[1].link_button("LinkedIn", profile["linkedin_url"])

                    st.divider()

        except Exception as e:
            st.error(f"Error searching profiles: {str(e)}")
