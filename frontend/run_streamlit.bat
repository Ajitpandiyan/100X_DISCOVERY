@echo off
REM Run Streamlit Application for 100X Discovery Platform
echo Starting 100X Discovery Platform...

REM Change to the correct directory if not already there
cd /d %~dp0

REM Run Streamlit application using global Python installation with port 8502
python -m streamlit run streamlit_app.py --server.port 8502

REM If the application exits with an error, pause to see the error message
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo An error occurred while running the application. 
    echo Please check the error message above.
    pause
) 