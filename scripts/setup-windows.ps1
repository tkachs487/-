$ErrorActionPreference = "Stop"
if (Get-Command py -ErrorAction SilentlyContinue) {
    py -3.11 -m venv .venv
} else {
    python -m venv .venv
}
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe scripts/check_environment.py
Write-Host "Windows Python environment ready. AGF Studio must be installed separately."
