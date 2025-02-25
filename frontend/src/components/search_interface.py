import streamlit as st

from ..utils.api import APIClient


def render_search_interface():
    st.header("Search Profiles")
    st.write("Powered by semantic search using Groq's LLM API")

    # Search input
    query = st.text_input(
        "Search by skills, interests, or keywords using natural language",
        placeholder="e.g., Machine learning expert with NLP skills",
    )

    # Advanced options
    with st.expander("Search Options"):
        st.caption(
            "The search uses semantic understanding to find the best matches based on:"
        )
        st.write("• Skills (weighted highest)")
        st.write("• Interests (weighted medium)")
        st.write("• Bio and name (weighted lower)")
        st.write("Results are ranked by relevance score (0-100)")

    # Backend connection status
    client = APIClient()
    
    if query:
        try:
            with st.spinner("Searching profiles with semantic search..."):
                results = client.search_profiles(query)
            
            # Check for error in results
            if "error" in results:
                st.error(f"Search failed: {results.get('error')}")
                st.info("Please try again later or contact support if the issue persists.")
                return

            if not results or len(results.get("matches", [])) == 0:
                st.info("No profiles found matching your search criteria.")
                return

            # Show search stats
            matches = results.get("matches", [])
            st.success(f"Found {len(matches)} relevant profiles for your search")

            # Display results
            for i, profile in enumerate(matches):
                with st.container():
                    # Create a card-like effect with background color
                    st.markdown(
                        f"""
                    <div class="profile-card">
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                    
                    # Profile header with name and score
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.subheader(profile.get("name", "Unknown"))
                    with col2:
                        score = int(profile.get("score", 0) * 100)
                        st.metric("Match", f"{score}%")
                    
                    # Bio
                    st.write(profile.get("bio", "No bio available"))
                    
                    # Skills and interests
                    if "skills" in profile and profile["skills"]:
                        st.write("**Skills:** " + ", ".join(profile["skills"]))
                    
                    if "interests" in profile and profile["interests"]:
                        st.write("**Interests:** " + ", ".join(profile["interests"]))
                    
                    # Links
                    cols = st.columns(2)
                    if "github_url" in profile and profile["github_url"]:
                        cols[0].markdown(f"[GitHub Profile]({profile['github_url']})")
                    
                    if "linkedin_url" in profile and profile["linkedin_url"]:
                        cols[1].markdown(f"[LinkedIn Profile]({profile['linkedin_url']})")
                    
                    # Match reason
                    if "match_reason" in profile and profile["match_reason"]:
                        with st.expander("Why this match?"):
                            st.write(profile["match_reason"])
                    
                    st.divider()
        except Exception as e:
            st.error(f"An error occurred during search: {str(e)}")
            st.info("Please try again later or contact support if the issue persists.")
