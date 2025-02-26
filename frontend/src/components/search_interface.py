import streamlit as st

from ..utils.api import APIClient


def display_search_results(results):
    """Display search results"""
    if not results or "matches" not in results:
        st.warning("No results found. Try a different search query.")
        if "error" in results:
            st.error(f"Error during search: {results['error']}")
        return
    
    matches = results["matches"]
    
    if not matches:
        st.warning("No profiles match your search criteria. Try a different query.")
        return
        
    st.success(f"Found {len(matches)} matching profiles")
    
    for i, profile in enumerate(matches):
        with st.expander(
            f"{i+1}. {profile['name']} - {int(profile['score'] * 100)}% match"
        ):
            st.markdown(f"**Bio:** {profile['bio']}")
            st.markdown(f"**Skills:** {', '.join(profile['skills'])}")
            st.markdown(f"**Interests:** {', '.join(profile['interests'])}")
            if "match_reason" in profile and profile["match_reason"]:
                st.markdown(f"**Match reason:** {profile['match_reason']}")
                
def run_search():
    """Run the search interface"""
    st.title("Search Profiles")
    
    query = st.text_input(
        "Enter search query",
        placeholder="E.g., Machine learning engineer with Python experience",
    )
    
    api_client = APIClient()
    
    if st.button("Search"):
        if not query:
            st.warning("Please enter a search query")
            return
            
        with st.spinner("Searching profiles..."):
            try:
                # Debug info
                st.info(f"Sending search request to backend: {query}")
                
                # Execute search
                results = api_client.search_profiles(query)
                
                # Display results
                display_search_results(results)
                
            except Exception as e:
                st.error(f"Error during search: {str(e)}")
                st.info("Please ensure the backend server is running at the correct URL")
                st.code(f"Backend URL: {settings.backend_api_url}")
    
    # Additional help for users
    with st.expander("Search Tips"):
        st.markdown("""
        - Use natural language to describe what you're looking for
        - Include specific skills, experience levels, or domains
        - Examples:
            - "Python developer with machine learning experience"
            - "Frontend engineer who knows React and TypeScript"
            - "Experienced data scientist with healthcare background"
        """)
