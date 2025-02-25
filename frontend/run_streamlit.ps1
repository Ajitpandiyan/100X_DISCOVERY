# Run Streamlit Application for 100X Discovery Platform
Write-Host "Starting 100X Discovery Platform..." -ForegroundColor Green

# Change to the script's directory if not already there
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
if ($scriptPath) {
    Set-Location -Path $scriptPath
}

try {
    # Run Streamlit application using python from virtual environment
    Write-Host "Launching Streamlit application..." -ForegroundColor Cyan
    & ".\venv_new\Scripts\python.exe" -m streamlit run streamlit_app.py
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