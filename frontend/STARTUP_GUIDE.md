# 100X Discovery Platform Startup Guide

This guide explains how to start the 100X Discovery Platform application using the provided scripts.

## Prerequisites

Before starting the application, ensure:

1. The virtual environment is set up correctly in the `venv_new` folder
2. All dependencies are installed (run `pip install -r requirements.txt` if needed)
3. The `.env` or `.env.local` file contains the necessary environment variables
4. The backend server is running (if not using the integrated mode)

## Starting the Application

You have two options to start the application:

### Option 1: Using the Batch File (Windows CMD)

1. Double-click the `run_streamlit.bat` file in Windows Explorer
2. Or open Command Prompt, navigate to the frontend directory, and run:
   ```
   run_streamlit.bat
   ```

### Option 2: Using the PowerShell Script

1. Right-click the `run_streamlit.ps1` file and select "Run with PowerShell"
2. Or open PowerShell, navigate to the frontend directory, and run:
   ```
   .\run_streamlit.ps1
   ```

## Troubleshooting

If you encounter errors:

1. Check that the virtual environment exists at `.\venv_new\`
2. Ensure all dependencies are installed within the virtual environment
3. Verify the backend server is running and accessible
4. Check that environment variables are correctly set in the `.env` or `.env.local` file

## Accessing the Application

Once started, the Streamlit application will be available at:
- http://localhost:8501

## Stopping the Application

To stop the application:
1. Press `Ctrl+C` in the terminal where it's running
2. Or close the terminal window 