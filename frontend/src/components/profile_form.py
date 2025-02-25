import streamlit as st
import uuid

from ..utils.api import APIClient


def render_profile_form():
    st.header("Create Your Profile")
    st.write("Add detailed information to improve semantic search matching")

    with st.form("profile_form"):
        name = st.text_input("Full Name*", placeholder="John Doe")
        
        # More detailed bio with guidance
        bio = st.text_area(
            "Bio*", 
            placeholder="Describe your experience, expertise, and what you're looking for...",
            help="A detailed bio helps the semantic search better understand your background and match you with relevant opportunities."
        )

        # Enhanced skills selection
        st.write("**Select or add your technical skills:**")
        predefined_skills = [
            "Python", "JavaScript", "TypeScript", "React", "Node.js", "Vue.js", "Angular",
            "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Data Science",
            "FastAPI", "Django", "Flask", "Express", "Spring Boot", "Docker", "Kubernetes",
            "AWS", "GCP", "Azure", "CI/CD", "DevOps", "SQL", "NoSQL", "MongoDB", "PostgreSQL",
            "Redis", "GraphQL", "REST API", "Microservices", "Serverless", "TensorFlow", "PyTorch"
        ]
        
        col1, col2 = st.columns(2)
        with col1:
            selected_skills = st.multiselect(
                "Skills from list*",
                options=predefined_skills,
                default=None,
                help="Select your technical skills from the predefined list."
            )
            
        with col2:
            custom_skills = st.text_input(
                "Additional Skills",
                placeholder="Comma-separated: Rust, Svelte, etc.",
                help="Add any skills not in the predefined list, separated by commas."
            )
        
        # Combine predefined and custom skills
        skills = selected_skills.copy()
        if custom_skills:
            custom_skills_list = [skill.strip() for skill in custom_skills.split(",") if skill.strip()]
            skills.extend(custom_skills_list)
        
        # Enhanced interests selection
        st.write("**Select or add your professional interests:**")
        predefined_interests = [
            "Web Development", "AI/ML", "Mobile Development", "Cloud Computing", 
            "Blockchain", "IoT", "Game Development", "AR/VR", "Cybersecurity",
            "Data Engineering", "Data Analytics", "UI/UX Design", "Product Management",
            "DevOps", "SRE", "Embedded Systems", "Fintech", "Healthtech", "Edtech",
            "Open Source", "Technical Writing", "Research", "Entrepreneurship"
        ]
        
        col1, col2 = st.columns(2)
        with col1:
            selected_interests = st.multiselect(
                "Interests from list*",
                options=predefined_interests,
                default=None,
                help="Select your professional interests from the predefined list."
            )
            
        with col2:
            custom_interests = st.text_input(
                "Additional Interests",
                placeholder="Comma-separated: Quantum Computing, etc.",
                help="Add any interests not in the predefined list, separated by commas."
            )
            
        # Combine predefined and custom interests
        interests = selected_interests.copy()
        if custom_interests:
            custom_interests_list = [interest.strip() for interest in custom_interests.split(",") if interest.strip()]
            interests.extend(custom_interests_list)
        
        # Links
        col1, col2 = st.columns(2)
        with col1:
            github_url = st.text_input(
                "GitHub Profile URL", 
                placeholder="https://github.com/yourusername"
            )
        with col2:
            linkedin_url = st.text_input(
                "LinkedIn Profile URL", 
                placeholder="https://linkedin.com/in/yourusername"
            )

        submitted = st.form_submit_button("Create Profile")

        if submitted:
            if not name or not bio or not skills or not interests:
                st.error("Name, bio, skills, and interests are required!")
                return

            # Generate a unique ID for the profile
            profile_id = str(uuid.uuid4())[:8]
            
            profile_data = {
                "id": profile_id,
                "name": name,
                "bio": bio,
                "skills": skills,
                "interests": interests,
                "github_url": github_url if github_url else None,
                "linkedin_url": linkedin_url if linkedin_url else None,
            }

            try:
                with st.spinner("Creating your profile..."):
                    client = APIClient()
                    response = client.create_profile(profile_data)
                
                st.success("Profile created successfully!")
                
                # Show confirmation with collapsible details
                with st.expander("Profile Details", expanded=True):
                    st.write(f"**Name:** {name}")
                    st.write(f"**Bio:** {bio}")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.write("**Skills:**")
                        for skill in skills:
                            st.write(f"- {skill}")
                            
                    with col2:
                        st.write("**Interests:**")
                        for interest in interests:
                            st.write(f"- {interest}")
                    
                    if github_url or linkedin_url:
                        st.write("**Links:**")
                        cols = st.columns(2)
                        if github_url:
                            cols[0].write(f"[GitHub]({github_url})")
                        if linkedin_url:
                            cols[1].write(f"[LinkedIn]({linkedin_url})")
                
                # Prompt to try the search
                st.info("Your profile is now searchable! Try out the search tab to see how semantic search works.")
                
            except Exception as e:
                st.error(f"Error creating profile: {str(e)}")
