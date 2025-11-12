@echo off
chcp 65001 >nul
echo ========================================
echo Sistema de Análisis de Préstamos con IA
echo ========================================
echo.

echo [1/3] Generando datos de entrenamiento...
echo ========================================
venv\Scripts\python.exe scripts\generar_datos_dummy.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Falló la generación de datos
    pause
    exit /b 1
)
echo ✓ Datos generados exitosamente (10,000 registros)
echo.

echo [2/3] Entrenando y comparando 3 modelos de IA...
echo ========================================
echo - Random Forest (Ensamble de Árboles)
echo - Gradient Boosting (XGBoost)
echo - Deep Learning (Red Neuronal Profunda)
echo.
venv\Scripts\python.exe scripts\entrenar_modelos_comparativa.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Falló el entrenamiento comparativo
    pause
    exit /b 1
)
echo.
echo ✓ 3 modelos entrenados y comparados
echo ✓ Mejor modelo seleccionado automáticamente
echo.

echo [3/3] Iniciando aplicación web con el mejor modelo...
echo ========================================
echo 🚀 La aplicación estará disponible en: http://localhost:5000
echo 📊 El sistema cargará automáticamente el modelo más eficiente
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
venv\Scripts\python.exe run.py

pause
