# Run both Backend and Frontend for 100X Discovery Platform
Write-Host "Starting 100X Discovery Platform..." -ForegroundColor Green

# Change to the script's directory if not already there
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($scriptPath) {
    Set-Location -Path $scriptPath
}

# Start the backend server in a new PowerShell window
$backendPath = Join-Path -Path (Split-Path -Parent $scriptPath) -ChildPath "backend"
Write-Host "Starting backend server at $backendPath..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-Command", "Set-Location '$backendPath'; python -m uvicorn app.main:app --reload --port 8000"

# Wait a moment for the backend to initialize
Write-Host "Waiting for backend to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

try {
    # Run Streamlit application using python from virtual environment with port 8502
    Write-Host "Launching Streamlit application on port 8502..." -ForegroundColor Cyan
    & ".\venv_new\Scripts\python.exe" -m streamlit run streamlit_app.py --server.port 8502
}
catch {
    Write-Host "An error occurred while running the application:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Read-Host -Prompt "Press Enter to exit"
}

# If the script reaches this point and the application exited with a non-zero status
if ($LASTEXITCODE -ne 0) {
    Write-Host "Application exited with error code: $LASTEXITCODE" -ForegroundColor Yellow
    Read-Host -Prompt "Press Enter to exit"
} 