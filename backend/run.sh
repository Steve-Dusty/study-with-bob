#!/bin/bash
# Quick start script for backend

echo "🚀 Starting Study With Bob Backend..."

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run server (no .env needed!)
echo "✅ No API keys required - using mock data!"
echo "Starting server..."
python main.py

