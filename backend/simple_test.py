"""Simple test script for semantic search functionality.

This script demonstrates the Groq-powered semantic search with a single query.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

from app.services.groq_service import GroqService
from app.services.profile_service import ProfileService

# Set test environment
os.environ["ENVIRONMENT"] = "test"

async def simple_test():
    """Test the semantic search functionality with a single query."""
    print("\n=== SEMANTIC SEARCH DEMO ===\n")
    
    # Initialize services
    profile_service = ProfileService()
    groq_service = GroqService()
    
    # Get existing profiles
    profiles = await profile_service.list_profiles()
    print(f"Found {len(profiles)} profiles in the database.\n")
    
    # Convert profiles to dictionaries for search
    profile_dicts = [profile.model_dump() for profile in profiles]
    
    # Test query
    query = "experienced React developer"
    print(f"Query: '{query}'")
    print("-" * 40)
    
    # Perform search
    results = await groq_service.get_semantic_search_results(query, profile_dicts)
    
    if results:
        print(f"Found {len(results)} matches:\n")
        for i, result in enumerate(results):
            print(f"Match #{i+1}: {result['name']} (Score: {result['score']})")
            print(f"Reason: {result['match_reason']}")
            
            # Format skills
            skills_text = ", ".join(result['skills'][:3])
            if len(result['skills']) > 3:
                skills_text += "..."
            print(f"Skills: {skills_text}")
            
            # Format bio
            bio = result['bio']
            if len(bio) > 80:
                bio = bio[:77] + "..."
            print(f"Bio: {bio}")
            print()
    else:
        print("No matches found.\n")
    
    print("=== DEMO COMPLETE ===\n")

if __name__ == "__main__":
    asyncio.run(simple_test()) 