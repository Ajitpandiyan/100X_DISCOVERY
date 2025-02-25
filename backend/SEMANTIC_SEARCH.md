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
    # Get all profiles
    profiles = await profile_service.list_profiles()
    
    # Convert profiles to dictionaries
    profile_dicts = [profile.dict() for profile in profiles]
    
    # Use Groq for semantic search
    matches = await groq_service.get_semantic_search_results(query, profile_dicts)

    return {"matches": matches}
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

If the Groq API is unavailable, the service falls back to a basic text-matching algorithm:

```python
def _fallback_search(self, query: str, profiles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Fallback search method using basic text matching if Groq API fails."""
    query = query.lower()
    matches = []
    
    for profile in profiles:
        profile_copy = profile.copy()
        score = 0
        
        # Check name (weight: 1)
        if query in profile_copy["name"].lower():
            score += 10
            
        # Check bio (weight: 1)
        if query in profile_copy["bio"].lower():
            score += 10
            
        # Check skills (weight: 2)
        for skill in profile_copy["skills"]:
            if query in skill.lower():
                score += 20
                
        # Check interests (weight: 1.5)
        for interest in profile_copy["interests"]:
            if query in interest.lower():
                score += 15
                
        if score > 0:
            profile_copy["score"] = score
            profile_copy["match_reason"] = "Text match"
            matches.append(profile_copy)
            
    # Sort by score
    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches
```

## Testing

The semantic search functionality is tested using pytest:

```bash
python -m pytest tests/test_semantic_search.py -v
```

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