@echo off
chcp 65001 >nul
echo ========================================
echo Iniciando aplicación web...
echo ========================================
echo.
echo La aplicación estará disponible en: http://localhost:5000
echo Presiona Ctrl+C para detener el servidor
echo.

venv\Scripts\python.exe run.py

pause
