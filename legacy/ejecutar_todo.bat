@echo off
echo ========================================
echo Sistema de Analisis de Prestamos con IA
echo ========================================
echo.
echo Este script ejecutara todo el proceso:
echo 1. Generar datos dummy
echo 2. Entrenar el modelo
echo 3. Probar el modelo
echo 4. Iniciar la interfaz web
echo.
pause

echo.
echo [1/4] Generando datos de entrenamiento...
echo ========================================
python generar_datos_dummy.py
if %errorlevel% neq 0 (
    echo ERROR: Fallo la generacion de datos
    pause
    exit /b 1
)

echo.
echo [2/4] Entrenando modelo de red neuronal...
echo ========================================
python entrenar_modelo.py
if %errorlevel% neq 0 (
    echo ERROR: Fallo el entrenamiento del modelo
    pause
    exit /b 1
)

echo.
echo [3/4] Ejecutando pruebas del modelo...
echo ========================================
python probar_modelo.py
if %errorlevel% neq 0 (
    echo ERROR: Fallaron las pruebas
    pause
    exit /b 1
)

echo.
echo [4/4] Iniciando interfaz de usuario...
echo ========================================
echo La aplicacion web se abrira en tu navegador
echo Presiona Ctrl+C para detener el servidor
echo.
streamlit run app_streamlit.py
