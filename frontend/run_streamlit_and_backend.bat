@echo off
REM Run both Backend and Frontend for 100X Discovery Platform
echo Starting 100X Discovery Platform...

REM Change to the frontend directory
cd /d %~dp0

REM First start the backend server in a new window
start cmd /k "cd /d %~dp0..\backend && python -m uvicorn app.main:app --reload --port 8000"

REM Wait a moment for the backend to initialize
echo Waiting for backend to start...
timeout /t 5 /nobreak > nul

REM Start the Streamlit frontend
echo Starting frontend...
python -m streamlit run streamlit_app.py --server.port 8502

REM If the application exits with an error, pause to see the error message
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred while running the application. 
    echo Please check the error message above.
    pause
) 