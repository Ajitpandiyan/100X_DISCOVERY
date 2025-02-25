# 100X Discovery Platform

A discovery platform for 100XEngineers AI cohort focusing on profile management and context-based search using Groq LLM.

## Project Structure
- `backend/`: FastAPI backend service
- `frontend/`: Streamlit frontend application
- `.github/`: CI/CD workflows

## Features

### Profile Management
- Create and manage detailed user profiles
- Store skills, interests, and professional background
- Link to GitHub and LinkedIn profiles

### Semantic Search (Powered by Groq)
- Find relevant profiles using natural language queries
- Intelligent matching based on skills, interests, and background
- Relevance scoring with explanations for matches
- Fallback mechanism for offline operation

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional)
- Groq API key (for semantic search)

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/100X_DISCOVERY.git
cd 100X_DISCOVERY
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

3. Start the backend:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

4. Start the frontend:
```bash
cd frontend
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Development

### Backend
The backend is built with FastAPI and provides REST APIs for profile management and search functionality.

#### Semantic Search Implementation
The semantic search feature uses Groq's LLM API to understand the meaning behind search queries and match them with relevant profiles:

1. **Query Processing**: Natural language queries are processed by the Groq LLM
2. **Profile Analysis**: The LLM analyzes profiles based on skills, interests, and background
3. **Relevance Scoring**: Profiles are ranked by relevance with explanations
4. **Fallback Mechanism**: Basic text matching is used if the Groq API is unavailable

To test the semantic search functionality:
```bash
cd backend
python test_semantic_search.py
```

### Frontend
The frontend is built with Streamlit and provides a clean, minimalist UI for profile creation and search.

## API Endpoints

### Profile Management
- `GET /api/v1/profiles/`: List all profiles
- `POST /api/v1/profiles/`: Create a new profile
- `GET /api/v1/profiles/{id}`: Get a specific profile
- `PUT /api/v1/profiles/{id}`: Update a profile
- `DELETE /api/v1/profiles/{id}`: Delete a profile

### Semantic Search
- `GET /api/v1/search/?query=your search query`: Search for profiles using semantic search
- `GET /api/v1/search/health`: Health check endpoint

## Deployment

### Backend (Koyeb)
Follow the deployment instructions in `backend/README.md`

### Frontend (Streamlit Cloud)
Follow the deployment instructions in `frontend/README.md`

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request