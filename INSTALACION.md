# 📦 Instalación y Configuración

## ✅ Prerequisitos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8 o superior** - [Descargar aquí](https://www.python.org/downloads/)
- **pip** (viene incluido con Python)
- **Git** (opcional) - Para clonar el repositorio

## 🔧 Instalación Completa

### Paso 1: Verificar Python

Abre PowerShell o CMD y verifica que Python esté instalado:

```bash
python --version
```

Deberías ver algo como: `Python 3.10.x` o superior

### Paso 2: Navegar al Directorio del Proyecto

```bash
cd "C:\Users\melca\Documents\Universidad 2025-2\loan-ai-system"
```

### Paso 3: Instalar Dependencias

Ejecuta el script batch de instalación:

```bash
instalar_dependencias.bat
```

Este instalará automáticamente:
- TensorFlow 2.15.0 (Deep Learning)
- Flask 3.0 (Framework web)
- Pandas, NumPy (Procesamiento de datos)
- Scikit-learn (Machine Learning)
- Faker (Generación de datos)

⏱️ **Tiempo estimado:** 2-5 minutos

### Paso 4: Ejecutar el Sistema

Una vez instaladas las dependencias, ejecuta:

```bash
iniciar_sistema.bat
```

Este script realizará:
1. Generación de datos de entrenamiento
2. Entrenamiento del modelo de IA
3. Pruebas de verificación
4. Inicio de la aplicación web

⏱️ **Tiempo estimado:** 8-12 minutos

### Paso 5: Acceder a la Aplicación

Una vez que veas el mensaje:
```
 * Running on http://0.0.0.0:5000
```

Abre tu navegador y accede a:
- **http://localhost:5000**
- o **http://127.0.0.1:5000**

## 🚀 Uso Diario

Para ejecutar la aplicación después de la instalación inicial:

```bash
iniciar_web.bat
```

## 📝 Instalación Manual (Alternativa)

Si prefieres instalar paso por paso:

### 1. Crear entorno virtual (Recomendado)

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Generar datos

```bash
python scripts\generar_datos_dummy.py
```

### 4. Entrenar modelo

```bash
python scripts\entrenar_modelo.py
```

### 5. Iniciar aplicación

```bash
python run.py
```

## 🐛 Solución de Problemas

### Error: "python no se reconoce como un comando"

**Solución:** Instala Python desde https://www.python.org/downloads/ y asegúrate de marcar "Add Python to PATH" durante la instalación.

### Error: "pip no se reconoce como un comando"

**Solución:** 
```bash
python -m ensurepip --upgrade
```

### Error durante instalación de TensorFlow

**Solución para Windows:**
1. Instala Microsoft Visual C++ Redistributable
2. Actualiza pip: `python -m pip install --upgrade pip`
3. Intenta de nuevo: `pip install tensorflow==2.15.0`

### Error: "PermissionError" al instalar

**Solución:** Ejecuta PowerShell o CMD como Administrador

### La aplicación no carga en el navegador

**Verificaciones:**
1. ¿El script sigue ejecutándose? No detengas el terminal
2. ¿Aparece algún error en el terminal?
3. ¿El puerto 5000 está disponible?
4. Intenta acceder a http://127.0.0.1:5000

### Puerto 5000 ocupado

**Solución:** Edita `run.py` y cambia el puerto:
```python
app.run(host='0.0.0.0', port=8080, debug=True)  # Cambiar 5000 por 8080
```

Luego accede a http://localhost:8080

## 📊 Verificación de Instalación

Después de ejecutar `iniciar_sistema.bat`, deberías tener:

```
loan-ai-system/
├── data/
│   └── datos_prestamos.csv          ✅ (10,000 registros)
├── models/
│   ├── modelo_prestamos_final.h5    ✅ (~50-100 MB)
│   ├── preprocessor.pkl             ✅
│   └── metricas_modelo.json         ✅
```

Verifica que estos archivos existan y tengan un tamaño razonable.

## 💡 Consejos de Rendimiento

### Para Computadoras Lentas

Si el entrenamiento es muy lento, edita `scripts\entrenar_modelo.py`:

```python
# Línea ~8: Cambiar
epochs = 100  # Por defecto
# A
epochs = 30   # Entrenamiento más rápido
```

### Para Acelerar Predicciones

La primera predicción es lenta porque carga el modelo. Las siguientes son instantáneas.

## 🔄 Actualización

Para actualizar las dependencias:

```bash
pip install --upgrade -r requirements.txt
```

## 🗑️ Desinstalación

Para remover completamente:

1. Elimina la carpeta del proyecto
2. Si creaste un entorno virtual, elimínalo:
   ```bash
   deactivate
   rmdir /s venv
   ```

## 📞 Soporte

Si encuentras problemas:

1. Verifica la sección de **Solución de Problemas** arriba
2. Revisa el archivo `INICIO_RAPIDO.md`
3. Consulta el `README.md`

## ✅ Checklist de Instalación

- [ ] Python 3.8+ instalado
- [ ] pip funcionando
- [ ] Dependencias instaladas (`instalar_dependencias.bat`)
- [ ] Datos generados (`data/datos_prestamos.csv`)
- [ ] Modelo entrenado (`models/modelo_prestamos_final.h5`)
- [ ] Aplicación web funciona (`http://localhost:5000`)

---

**¡Todo listo! 🎉**

Ahora puedes usar el sistema de análisis de préstamos con IA.
