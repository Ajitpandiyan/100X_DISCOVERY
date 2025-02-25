# 100X Discovery Platform Frontend

Streamlit frontend for the 100X Discovery Platform with semantic search capabilities.

## Features

- **Profile Creation**: Create detailed user profiles with skills, interests, and links
- **Semantic Search**: Find relevant profiles using natural language queries powered by Groq's LLM API
- **Responsive Design**: Light/dark mode and mobile-friendly UI

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
STREAMLIT_TOKEN=your_streamlit_token
BACKEND_API_KEY=your_backend_api_key
BACKEND_API_URL=http://localhost:8000  # Local backend URL
```

4. Run the application:
```bash
streamlit run streamlit_app.py
```

## Semantic Search

The platform uses Groq's LLM API (via the backend) to provide intelligent semantic search capabilities:

### How It Works

1. **User Profiles**: Create detailed profiles with skills, interests, and background information
2. **Natural Language Search**: Search using natural language queries like "experienced React developer with ML knowledge"
3. **Relevance Scores**: Results include relevance scores and explanations for matches
4. **Advanced Options**: View detailed information about how the search works

### Example Queries

Try searching with natural language queries like:

- "experienced React developer"
- "machine learning expert with NLP skills"
- "cloud infrastructure specialist"
- "mobile app developer with cross-platform experience"
- "data scientist with finance background"

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

The frontend is configured for deployment on Streamlit Cloud. Set the following secrets in Streamlit Cloud:

- `STREAMLIT_TOKEN`: Your Streamlit API token
- `BACKEND_API_KEY`: Your backend API key
- `BACKEND_API_URL`: Your backend URL (e.g., https://100x-discovery-backend-ajitpandiyan.koyeb.app)