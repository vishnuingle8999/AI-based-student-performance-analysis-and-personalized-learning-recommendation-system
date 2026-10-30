@echo off
title AI-Based Student Learning Recommendation System
echo =====================================================================
echo  AI-Based Personalized Student Learning Recommendation System
echo =====================================================================
echo.
echo [1/3] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not added to PATH!
    echo Please install Python 3.10+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b
)

echo [2/3] Installing / Verifying required packages...
pip install -r requirements.txt

echo.
echo [3/3] Launching Web Application...
echo.
echo Opening browser in 3 seconds at http://127.0.0.1:5000 ...
timeout /t 3 /nobreak >nul
start http://127.0.0.1:5000

echo.
echo =====================================================================
echo  Server is running! Press Ctrl+C in this window to stop the server.
echo =====================================================================
echo.
python app.py

pause
