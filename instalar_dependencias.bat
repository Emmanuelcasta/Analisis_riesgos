@echo off
chcp 65001 >nul
echo ========================================
echo Instalando dependencias...
echo ========================================
echo.

pip install -r requirements.txt

if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Falló la instalación de dependencias
    pause
    exit /b 1
)

echo.
echo ✓ Todas las dependencias instaladas correctamente
echo.
pause
