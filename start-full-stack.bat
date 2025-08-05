@echo off
echo Starting Oshioxi Full Stack Application...
echo.

echo Starting Backend Django Server...
start "Django Backend" cmd /k "cd backend && python start.py"

echo Waiting for backend to start...
timeout /t 5

echo Starting Frontend React App...
start "React Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ===================================
echo Full Stack Application Started!
echo ===================================
echo.
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:5173
echo Django Admin: http://127.0.0.1:8000/admin/
echo API Documentation: http://127.0.0.1:8000/api/v1/
echo.
echo Press any key to close all applications...
pause > nul

echo Closing applications...
taskkill /F /IM cmd.exe /FI "WINDOWTITLE eq Django Backend"
taskkill /F /IM cmd.exe /FI "WINDOWTITLE eq React Frontend"