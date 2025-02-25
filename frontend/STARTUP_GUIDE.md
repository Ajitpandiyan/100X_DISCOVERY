# 100X Discovery Platform - Startup Guide

This guide provides instructions for setting up and running the 100X Discovery Platform on your local machine.

## Prerequisites

- Python 3.9 or higher
- Git (for cloning the repository)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/100X_DISCOVERY.git
cd 100X_DISCOVERY
```

### 2. Backend Setup

```bash
cd backend

# Create a virtual environment
python -m venv venv_new

# Activate the virtual environment
# On Windows:
.\venv_new\Scripts\activate
# On macOS/Linux:
# source venv_new/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file (copy from .env.example)
# Make sure to set the GROQ_API_KEY if needed
```

### 3. Frontend Setup

```bash
cd ../frontend

# Create a virtual environment
python -m venv venv_new

# Activate the virtual environment
# On Windows:
.\venv_new\Scripts\activate
# On macOS/Linux:
# source venv_new/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create a .env file (copy from .env.example)
```

## Running the Application

### Option 1: Using the Provided Scripts (Recommended)

#### Windows Users:

**PowerShell:**
```
.\run_streamlit_and_backend.ps1
```

**Command Prompt:**
```
run_streamlit_and_backend.bat
```

#### macOS/Linux Users:
```bash
./run_streamlit_and_backend.sh
```

### Option 2: Manual Startup

#### Start the Backend:
```bash
cd backend
# Activate virtual environment if not already activated
python -m uvicorn app.main:app --reload --port 8000
```

#### Start the Frontend (in a new terminal):
```bash
cd frontend
# Activate virtual environment if not already activated
python -m streamlit run streamlit_app.py --server.port 8502
```

## Accessing the Application

- Frontend: http://localhost:8502
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Troubleshooting

### Connection Issues

If you see "Could not connect to backend server" errors:

1. Ensure the backend server is running on port 8000
2. Check that your `.env` file in the frontend directory has:
   ```
   BACKEND_API_URL=http://localhost:8000
   ```
3. Verify that the backend's CORS settings include your frontend URL:
   ```
   BACKEND_CORS_ORIGINS=["http://localhost:8501", "http://localhost:8502"]
   ```

### Python Path Issues

If you encounter "module not found" errors:
- Make sure you're using the correct virtual environment
- Try installing the missing package: `pip install <package_name>`

### Port Already in Use

If port 8000 or 8502 is already in use:
- Change the port in the run commands
- Update the CORS settings and environment variables accordingly 