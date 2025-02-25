"""Test script for semantic search functionality.

This script demonstrates how to use the Groq-powered semantic search
to find relevant profiles based on natural language queries.
"""

import asyncio
import json
import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

from app.models.profile import ProfileCreate
from app.services.groq_service import GroqService
from app.services.profile_service import ProfileService

# Set test environment
os.environ["ENVIRONMENT"] = "test"


async def test_semantic_search():
    """Test the semantic search functionality with sample profiles."""
    print("\n=== SEMANTIC SEARCH TEST ===\n")

    # Initialize services
    profile_service = ProfileService()
    groq_service = GroqService()

    # Create sample profiles if none exist
    profiles = await profile_service.list_profiles()

    if not profiles:
        print("Creating sample profiles...")

        # Clear existing profiles first
        await profile_service._write_profiles([])

        # Sample profiles with diverse backgrounds
        sample_profiles = [
            ProfileCreate(
                id="1",
                name="Alex Johnson",
                bio="Senior frontend developer with 5+ years experience in React and modern JavaScript frameworks. Passionate about creating responsive and accessible user interfaces.",
                skills=[
                    "React",
                    "JavaScript",
                    "TypeScript",
                    "CSS",
                    "Accessibility",
                    "Redux",
                ],
                interests=["Web Development", "UI/UX Design", "Open Source"],
                github_url="https://github.com/alexj",
                linkedin_url="https://linkedin.com/in/alexj",
            ),
            ProfileCreate(
                id="2",
                name="Priya Sharma",
                bio="Machine learning engineer specializing in NLP and computer vision. Experience with PyTorch and TensorFlow. PhD in Computational Linguistics.",
                skills=[
                    "Python",
                    "PyTorch",
                    "TensorFlow",
                    "NLP",
                    "Machine Learning",
                    "Deep Learning",
                ],
                interests=[
                    "Artificial Intelligence",
                    "Natural Language Processing",
                    "Research",
                ],
                github_url="https://github.com/priyasharma",
                linkedin_url="https://linkedin.com/in/priyasharma",
            ),
            ProfileCreate(
                id="3",
                name="Carlos Rodriguez",
                bio="DevOps engineer with expertise in cloud infrastructure and containerization. AWS certified solutions architect with experience in Kubernetes and Docker.",
                skills=["AWS", "Kubernetes", "Docker", "Terraform", "CI/CD", "Linux"],
                interests=[
                    "Cloud Computing",
                    "Infrastructure as Code",
                    "Site Reliability",
                ],
                github_url="https://github.com/carlosr",
                linkedin_url="https://linkedin.com/in/carlosr",
            ),
            ProfileCreate(
                id="4",
                name="Mei Lin",
                bio="Full-stack mobile developer with experience in React Native and Flutter. Passionate about creating cross-platform mobile experiences with native performance.",
                skills=[
                    "React Native",
                    "Flutter",
                    "JavaScript",
                    "Dart",
                    "iOS",
                    "Android",
                ],
                interests=["Mobile Development", "Cross-Platform Apps", "UI Animation"],
                github_url="https://github.com/meilin",
                linkedin_url="https://linkedin.com/in/meilin",
            ),
            ProfileCreate(
                id="5",
                name="David Kim",
                bio="Data scientist with background in finance and statistics. Experience with predictive modeling, data visualization, and machine learning for financial applications.",
                skills=["Python", "R", "SQL", "Pandas", "Scikit-learn", "Tableau"],
                interests=[
                    "Data Science",
                    "Financial Analysis",
                    "Statistical Modeling",
                ],
                github_url="https://github.com/davidkim",
                linkedin_url="https://linkedin.com/in/davidkim",
            ),
        ]

        # Add sample profiles
        for profile in sample_profiles:
            await profile_service.create_profile(profile)

        # Verify profiles were created
        profiles = await profile_service.list_profiles()
        print(f"Sample profiles created! Total profiles: {len(profiles)}")
    else:
        print(f"Using existing profiles. Total profiles: {len(profiles)}")

    # Convert profiles to dictionaries for search
    profile_dicts = [profile.model_dump() for profile in profiles]

    # Test queries
    test_queries = [
        "experienced React developer",
        "machine learning expert with NLP skills",
        "cloud infrastructure specialist",
        "mobile app developer with cross-platform experience",
        "data scientist with finance background",
    ]

    # Run searches
    print("\n=== SEARCH RESULTS ===\n")

    for i, query in enumerate(test_queries):
        print(f"Query #{i+1}: '{query}'")
        print("-" * 40)

        try:
            results = await groq_service.get_semantic_search_results(
                query, profile_dicts
            )

            if results:
                print(f"Found {len(results)} matches:\n")
                for j, result in enumerate(results):
                    print(
                        f"  Match #{j+1}: {result['name']} (Score: {result['score']})"
                    )
                    print(f"  Reason: {result['match_reason']}")

                    # Format skills with proper truncation
                    skills = result['skills'][:3]
                    skills_text = ", ".join(skills)
                    if len(result['skills']) > 3:
                        skills_text += "..."
                    print(f"  Skills: {skills_text}")

                    # Format bio with proper truncation
                    bio = result['bio']
                    if len(bio) > 80:
                        bio = bio[:77] + "..."
                    print(f"  Bio: {bio}")
                    print()
            else:
                print("No matches found.\n")
        except Exception as e:
            print(f"Error during search: {str(e)}\n")

        print("=" * 40)
        print()

    print("=== TEST COMPLETE ===\n")


if __name__ == "__main__":
    asyncio.run(test_semantic_search())
