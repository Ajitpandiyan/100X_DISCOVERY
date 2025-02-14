# 100X Discovery Platform

## Deployment URLs

- Frontend: https://100x-discovery.streamlit.app
- Backend API: https://100x-discovery-api-your-name.koyeb.app

## GitHub Repository
https://github.com/yourusername/100X_DISCOVERY

## Development Workflow

1. Clone the repository:
```bash
git clone https://github.com/yourusername/100X_DISCOVERY.git
cd 100X_DISCOVERY
```

2. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit:
```bash
git add .
git commit -m "Description of your changes"
```

4. Push to GitHub:
```bash
git push origin feature/your-feature-name
```

5. Create a Pull Request on GitHub

## CI/CD

The project uses GitHub Actions for:
- Running tests
- Deploying to Koyeb (backend)
- Deploying to Streamlit Cloud (frontend)

### Required Secrets
- GROQ_API_KEY
- KOYEB_TOKEN
- STREAMLIT_API_KEY

## Local Development

1. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your values
```

3. Run with Docker:
```bash
docker-compose up --build
```

4. Access the application:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000

## Production Deployment

### Backend (Koyeb)
```bash
./scripts/deploy-koyeb.sh
```

### Frontend (Streamlit Cloud)
Push to main branch and Streamlit Cloud will automatically deploy.

## Environment Variables

### Backend
- `GROQ_API_KEY`: Your Groq API key
- `PORT`: Server port (default: 8000)
- `DATA_DIR`: Directory for JSON storage

### Frontend
- `BACKEND_URL`: URL of the backend API 
