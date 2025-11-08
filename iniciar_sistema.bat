@echo off
chcp 65001 >nul
echo ========================================
echo Sistema de Análisis de Préstamos con IA
echo ========================================
echo.

echo [1/4] Generando datos de entrenamiento...
echo ========================================
venv\Scripts\python.exe scripts\generar_datos_dummy.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Falló la generación de datos
    pause
    exit /b 1
)
echo ✓ Datos generados exitosamente
echo.

echo [2/4] Entrenando modelo de IA...
echo ========================================
venv\Scripts\python.exe scripts\entrenar_modelo.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Falló el entrenamiento del modelo
    pause
    exit /b 1
)
echo ✓ Modelo entrenado exitosamente
echo.

echo [3/4] Probando modelo...
echo ========================================
venv\Scripts\python.exe scripts\probar_modelo.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Falló la prueba del modelo
    pause
    exit /b 1
)
echo ✓ Modelo probado exitosamente
echo.

echo [4/4] Iniciando aplicación web...
echo ========================================
echo La aplicación estará disponible en: http://localhost:5000
echo Presiona Ctrl+C para detener el servidor
echo.
venv\Scripts\python.exe run.py

pause
