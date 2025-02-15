# 100X Discovery Platform

A discovery platform for 100XEngineers AI cohort focusing on profile management and context-based search using Groq LLM.

## Project Structure
- `backend/`: FastAPI backend service
- `frontend/`: Streamlit frontend application
- `.github/`: CI/CD workflows

## Getting Started

### Prerequisites
- Python 3.9+
- Docker (optional)

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

### Frontend
The frontend is built with Streamlit and provides a clean, minimalist UI for profile creation and search.

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