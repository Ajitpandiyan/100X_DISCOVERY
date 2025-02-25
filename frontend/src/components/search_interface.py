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
        st.caption("The search uses semantic understanding to find the best matches based on:")
        st.write("• Skills (weighted highest)")  
        st.write("• Interests (weighted medium)")
        st.write("• Bio and name (weighted lower)")
        st.write("Results are ranked by relevance score (0-100)")

    if query:
        try:
            with st.spinner("Searching profiles with semantic search..."):
                client = APIClient()
                results = client.search_profiles(query)

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
                    st.markdown(f"""
                    <div class="profile-card">
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Match information
                    match_score = profile.get("score", 0)
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.subheader(profile["name"])
                        
                    with col2:
                        # Display score with a progress bar
                        if match_score:
                            st.metric("Match Score", f"{int(match_score)}/100")
                    
                    # Match reason
                    if "match_reason" in profile and profile["match_reason"]:
                        st.info(f"**Why this match?** {profile['match_reason']}")
                    
                    # Profile details
                    st.write(profile["bio"])
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.write("**Skills:**")
                        for skill in profile["skills"]:
                            st.markdown(f"- {skill}")

                    with col2:
                        st.write("**Interests:**")
                        for interest in profile["interests"]:
                            st.markdown(f"- {interest}")

                    # Links
                    if profile.get("github_url") or profile.get("linkedin_url"):
                        st.write("**Links:**")
                        cols = st.columns(2)
                        if profile.get("github_url"):
                            cols[0].link_button("GitHub", profile["github_url"])
                        if profile.get("linkedin_url"):
                            cols[1].link_button("LinkedIn", profile["linkedin_url"])

                    st.divider()

        except Exception as e:
            st.error(f"Error searching profiles: {str(e)}")
            st.write("Please ensure the backend server is running and properly configured.")
