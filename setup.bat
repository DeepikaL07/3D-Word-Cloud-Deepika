@echo off
echo ============================================
echo 3D Word Cloud Setup Script
echo ============================================
echo.

REM Install backend dependencies
echo [1/4] Installing backend dependencies...
cd backend
python -m pip install -r requirements.txt
cd ..

REM Install frontend dependencies
echo.
echo [2/4] Installing frontend dependencies...
cd frontend
call npm install
cd ..

echo.
echo [3/4] Setup complete!
echo.
echo [4/4] Starting servers...
echo.

REM Start both servers
start cmd /k "cd backend && venv\Scripts\activate && uvicorn main:app --reload"
timeout /t 3 >nul
start cmd /k "cd frontend && npm start"

echo Both servers are starting!
pause
