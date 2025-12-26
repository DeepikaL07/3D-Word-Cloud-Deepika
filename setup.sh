#!/bin/bash

echo "============================================"
echo "3D Word Cloud Setup Script"
echo "============================================"

echo "[1/4] Installing backend dependencies..."
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

echo "[2/4] Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "[3/4] Setup complete!"
echo "[4/4] Starting servers..."

cd backend
source venv/bin/activate
uvicorn main:app --reload &
BACKEND_PID=$!

cd ../frontend
npm start &
FRONTEND_PID=$!

wait
kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
