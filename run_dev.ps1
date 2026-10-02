Write-Host "Starting MedGuidance Backend in Virtual Environment (.venv)..." -ForegroundColor Cyan
& ".\.venv\Scripts\uvicorn.exe" app.main:app --reload --host 127.0.0.1 --port 8000
