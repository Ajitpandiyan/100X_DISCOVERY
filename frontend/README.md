# 100X Discovery Platform - Frontend

A modern web application built with Streamlit for discovering and connecting with talented engineers.

## Features
- Create and manage professional profiles
- Search for engineers based on skills and interests
- AI-powered profile matching
- Real-time updates

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run streamlit_app.py
```

## Environment Variables
Copy `.env.example` to `.env` and fill in your values:
- `STREAMLIT_TOKEN`: Your Streamlit API token
- `BACKEND_API_URL`: Backend API URL
- `BACKEND_API_KEY`: Backend API authentication key

## Deployment
The application is automatically deployed to Streamlit Cloud via GitHub Actions when changes are pushed to the main branch.