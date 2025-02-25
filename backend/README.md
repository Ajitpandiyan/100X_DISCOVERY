# 100X Discovery Platform Backend

FastAPI backend service for the 100X Discovery Platform with semantic search capabilities powered by Groq.

## Features

- **Profile Management**: Create, read, update, and delete user profiles
- **Semantic Search**: Find relevant profiles using natural language queries
- **Groq Integration**: Leverage Groq's LLM API for intelligent profile matching

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file with the following variables
GROQ_API_KEY=your_groq_api_key
BACKEND_CORS_ORIGINS=["http://localhost:8501", "https://*.streamlit.app"]
ENVIRONMENT=development
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## Semantic Search

The platform uses Groq's LLM API to provide intelligent semantic search capabilities:

### How It Works

1. **Profile Indexing**: User profiles are stored with their skills, interests, and other attributes
2. **Query Processing**: When a search query is received, it's sent to Groq's LLM API
3. **Semantic Matching**: The LLM analyzes the query and profiles to find semantic matches
4. **Relevance Scoring**: Each profile is assigned a relevance score and explanation
5. **Fallback Mechanism**: If the Groq API is unavailable, a basic text-matching algorithm is used

### Testing Semantic Search

You can test the semantic search functionality using the provided scripts:

```bash
# Full test with multiple queries
python test_semantic_search.py

# Simple demo with a single query
python simple_test.py
```

These scripts will:
1. Use existing profiles or create sample profiles if none exist
2. Run test queries against the profiles
3. Display the matching profiles with their relevance scores and explanations

Example output:
```
=== SEMANTIC SEARCH DEMO ===

Found 5 profiles in the database.

Query: 'experienced React developer'
----------------------------------------
Using fallback search for testing...
Found 2 matches:

Match #1: Alex Chen (Score: 75)
Reason: Bio contains relevant terms; Skills match: React; Role 'developer' matches
Skills: JavaScript, React, Node.js...
Bio: Full-stack developer with 5 years of experience in React and Node.js

Match #2: Sofia Rodriguez (Score: 50)
Reason: Bio contains relevant terms; Skills match: React Native; Role 'developer' matches
Skills: Flutter, React Native, Swift...
Bio: Mobile app developer focused on cross-platform solutions
```

### API Endpoints

- `GET /api/v1/search/?query=your search query`: Search for profiles using semantic search
- `GET /api/v1/search/health`: Health check endpoint

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
isort .
```

## Deployment

The backend is configured for deployment on Koyeb. Set the following environment variables in your Koyeb deployment:

- `GROQ_API_KEY`: Your Groq API key
- `BACKEND_CORS_ORIGINS`: Allowed origins for CORS (e.g., `["https://your-streamlit-app.streamlit.app"]`)
- `ENVIRONMENT`: Set to `production`