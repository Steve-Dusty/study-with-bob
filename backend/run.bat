@echo off
REM Quick start script for backend on Windows

echo 🚀 Starting Study With Bob Backend...

REM Check if venv exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Run server (no .env needed!)
echo ✅ No API keys required - using mock data!
echo Starting server...
python main.py

