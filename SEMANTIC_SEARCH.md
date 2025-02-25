# Semantic Search Implementation

This document describes the semantic search implementation in the 100X Discovery Platform.

## Overview

The platform uses Groq's LLM API to provide intelligent semantic search capabilities for finding relevant user profiles based on natural language queries.

## Components

1. **GroqService**: A service that interacts with Groq's LLM API to perform semantic search
2. **Search Router**: API endpoints for searching profiles using semantic search
3. **Test Suite**: Tests for the semantic search functionality

## How It Works

### 1. Query Processing

When a user submits a search query, the search router receives the request and passes it to the GroqService.

```python
@router.get("/")
async def search_profiles(
    query: str = Query(..., description="Search query for matching profiles")
) -> Dict[str, List[Dict[str, Any]]]:
    """Search for profiles based on a text query using semantic search."""
    try:
        # Get all profiles
        profiles = await profile_service.list_profiles()
        
        # Convert profiles to dictionaries
        profile_dicts = [profile.model_dump() for profile in profiles]
        
        # Use Groq for semantic search
        matches = await groq_service.get_semantic_search_results(query, profile_dicts)

        return {"matches": matches}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to search profiles: {str(e)}",
        )
```

### 2. Semantic Matching

The GroqService formats the profiles and query into a prompt for the Groq LLM API:

```python
# Format profiles for the prompt
profiles_text = "\n\n".join(
    [
        f"Profile {i+1}:\nName: {p['name']}\nBio: {p['bio']}\n"
        f"Skills: {', '.join(p['skills'])}\n"
        f"Interests: {', '.join(p['interests'])}"
        for i, p in enumerate(profiles)
    ]
)

# Create prompt for semantic search
prompt = f"""
I have the following user profiles:

{profiles_text}

Search query: "{query}"

Analyze these profiles and rank them by relevance to the search query.
Consider skills, interests, bio, and name, with skills being most important.
Return a JSON array of objects with profile index (starting from 1) and relevance score (0-100).
Only include profiles with some relevance (score > 0).
Format: [{{\"profile_index\": 1, \"score\": 85, \"reasoning\": \"brief explanation\"}}]
"""
```

### 3. LLM Processing

The Groq LLM analyzes the profiles and query, understanding the semantic meaning behind them. It returns a JSON response with:

- Profile indices
- Relevance scores (0-100)
- Reasoning for each match

### 4. Result Processing

The GroqService processes the LLM response, maps it back to the original profiles, and returns the results:

```python
# Map the results back to the original profiles
ranked_profiles = []
for result in search_results.get("results", []):
    profile_idx = result.get("profile_index", 0) - 1
    if 0 <= profile_idx < len(profiles):
        profile_copy = profiles[profile_idx].copy()
        profile_copy["score"] = result.get("score", 0)
        profile_copy["match_reason"] = result.get("reasoning", "")
        ranked_profiles.append(profile_copy)

# Sort by score (highest first)
ranked_profiles.sort(key=lambda x: x["score"], reverse=True)
return ranked_profiles
```

### 5. Fallback Mechanism

If the Groq API is unavailable or in test mode, the service falls back to a basic text-matching algorithm:

```python
def _fallback_search(self, query: str, profiles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Fallback search method using basic text matching if Groq API fails."""
    query = query.lower()
    matches = []
    
    # Split query into terms for better matching
    query_terms = query.lower().split()
    
    for profile in profiles:
        profile_copy = profile.copy()
        score = 0
        match_reason = []
        
        # Check name (weight: 1)
        if any(term in profile_copy["name"].lower() for term in query_terms):
            score += 10
            match_reason.append(f"Name matches search terms")
            
        # Check bio (weight: 1)
        bio_matches = [term for term in query_terms if term in profile_copy["bio"].lower()]
        if bio_matches:
            score += len(bio_matches) * 5
            match_reason.append(f"Bio contains relevant terms")
        
        # Check skills (weight: 2)
        skill_matches = []
        for skill in profile_copy["skills"]:
            skill_lower = skill.lower()
            for term in query_terms:
                if term in skill_lower:
                    score += 20
                    skill_matches.append(skill)
                    break
        
        if skill_matches:
            match_reason.append(f"Skills match: {', '.join(skill_matches[:2])}")
                
        # Check interests (weight: 1.5)
        interest_matches = []
        for interest in profile_copy["interests"]:
            interest_lower = interest.lower()
            for term in query_terms:
                if term in interest_lower:
                    score += 15
                    interest_matches.append(interest)
                    break
        
        if interest_matches:
            match_reason.append(f"Interests match: {', '.join(interest_matches[:2])}")
        
        # Check for specific role matches
        roles = ["developer", "engineer", "scientist", "designer", "manager", "specialist", "expert"]
        for role in roles:
            if role in query.lower() and role in profile_copy["bio"].lower():
                score += 25
                match_reason.append(f"Role '{role}' matches")
        
        # Add semantic-like matching for common terms
        semantic_matches = {
            "ml": ["machine learning", "deep learning", "ai", "artificial intelligence", "neural networks"],
            "ai": ["artificial intelligence", "machine learning", "deep learning", "neural networks"],
            "frontend": ["ui", "user interface", "react", "angular", "vue", "javascript", "web"],
            "backend": ["server", "api", "database", "node", "django", "flask", "fastapi"],
            "cloud": ["aws", "azure", "gcp", "infrastructure", "devops", "kubernetes", "docker"],
            "mobile": ["ios", "android", "flutter", "react native", "cross-platform"],
            "data": ["analytics", "visualization", "science", "scientist", "analysis", "statistics"]
        }
        
        # Special case for experience level terms
        experience_terms = ["experienced", "senior", "expert", "specialist", "professional"]
        if any(term in query.lower() for term in experience_terms) and any(term in profile_copy["bio"].lower() for term in ["years", "experience", "senior"]):
            score += 20
            match_reason.append("Experience level matches")
        
        if score > 0:
            profile_copy["score"] = min(score, 100)  # Cap score at 100
            profile_copy["match_reason"] = "; ".join(match_reason[:3])  # Limit to top 3 reasons
            matches.append(profile_copy)
            
    # Sort by score
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches
```

## Testing

The semantic search functionality can be tested using the provided script:

```bash
python test_semantic_search.py
```

This script:
1. Creates sample profiles if none exist
2. Runs several test queries against the profiles
3. Displays the matching profiles with their relevance scores and explanations

## Example Queries

The semantic search can handle various types of queries:

- "experienced React developer"
- "machine learning expert with NLP skills"
- "cloud infrastructure specialist"
- "mobile app developer with cross-platform experience"
- "data scientist with finance background"

## Future Improvements

1. **Vector Embeddings**: Store profile embeddings for faster search
2. **Query Expansion**: Expand queries to include related terms
3. **Hybrid Search**: Combine semantic search with keyword search
4. **User Feedback**: Incorporate user feedback to improve search results
5. **Caching**: Cache common search results for better performance 