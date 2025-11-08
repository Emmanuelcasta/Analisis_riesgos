# 🚀 Guía de Inicio Rápido# Guía de Uso Rápido



## ⚡ Opción 1: Ejecutar Todo Automáticamente (RECOMENDADO)## Opción 1: Ejecutar Todo Automáticamente



Simplemente ejecuta:Ejecuta este comando en PowerShell:



```bash```powershell

iniciar_sistema.batcd C:\loan-ai-system

```.\ejecutar_todo.bat

```

Este script realiza automáticamente:

1. ✅ Generación de 10,000 datos de entrenamientoEste script ejecutará automáticamente:

2. ✅ Entrenamiento del modelo de IA1. ✅ Generación de datos dummy

3. ✅ Pruebas de verificación2. ✅ Entrenamiento del modelo

4. ✅ Lanzamiento de la aplicación web en http://localhost:50003. ✅ Pruebas de verificación

4. ✅ Lanzamiento de la interfaz web

## 🔧 Opción 2: Ejecutar Paso por Paso

## Opción 2: Ejecutar Paso por Paso

### 1. Instalar Dependencias

### 1. Instalar dependencias

```bash

instalar_dependencias.bat```powershell

```pip install -r requirements.txt

```

O manualmente:

### 2. Generar datos

```bash

pip install -r requirements.txt```powershell

```python generar_datos_dummy.py

```

### 2. Generar Datos de Entrenamiento

### 3. Entrenar modelo

```bash

python scripts\generar_datos_dummy.py```powershell

```python entrenar_modelo.py

```

Crea: `data/datos_prestamos.csv` (10,000 registros)

### 4. Probar modelo

### 3. Entrenar el Modelo

```powershell

```bashpython probar_modelo.py

python scripts\entrenar_modelo.py```

```

### 5. Iniciar interfaz web

Genera:

- `models/modelo_prestamos_final.h5````powershell

- `models/preprocessor.pkl`streamlit run app_streamlit.py

- `models/metricas_modelo.json````



### 4. Probar el Modelo## ⏱️ Tiempos Estimados



```bash- Generación de datos: ~30 segundos

python scripts\probar_modelo.py- Entrenamiento del modelo: ~3-5 minutos

```- Pruebas: ~10 segundos

- Inicio de interfaz: ~5 segundos

### 5. Iniciar la Aplicación Web

## 🌐 Acceder a la Aplicación

```bash

iniciar_web.batUna vez iniciada, abre tu navegador en:

```

**http://localhost:8501**

O con Python:

## ❓ Solución de Problemas

```bash

python run.py### Error: "No module named 'tensorflow'"

```

```powershell

Accede a: **http://localhost:5000**pip install tensorflow==2.15.0

```

## ⏱️ Tiempos Estimados

### Error: "No module named 'streamlit'"

| Paso | Tiempo |

|------|--------|```powershell

| Instalación de dependencias | 2-5 minutos |pip install streamlit

| Generación de datos | 30-60 segundos |```

| Entrenamiento del modelo | 3-5 minutos |

| Pruebas | 10-20 segundos |### Error: "Model file not found"

| Inicio de la web | 5-10 segundos |

Asegúrate de haber ejecutado primero:

**Total:** ~10 minutos aproximadamente

```powershell

## 🌐 Uso de la Aplicación Webpython entrenar_modelo.py

```

1. Abre tu navegador en http://localhost:5000

2. Completa el formulario de solicitud de préstamo## 📧 Soporte

3. Haz clic en "Analizar Solicitud"

4. Revisa los resultados:Si encuentras problemas, revisa el archivo `README.md` completo para más detalles.

   - Probabilidad de aprobación
   - Decisión (Aprobado/Rechazado)
   - Nivel de riesgo
   - Análisis financiero detallado
   - Recomendaciones personalizadas

## 📝 Estructura del Formulario

### Paso 1: Datos Generales
- Información personal (nombre, documento, contacto)
- Fecha de nacimiento
- Dirección y residencia

### Paso 2: Información Personal y Laboral
- Estado civil y dependientes
- Nivel educativo
- Ocupación y tipo de contrato
- Sector económico y experiencia

### Paso 3: Información Financiera
- Ingresos mensuales (principal y adicionales)
- Gastos mensuales
- Monto del préstamo solicitado
- Plazo en meses
- Línea de crédito

## 🎯 Ejemplo de Datos de Prueba

Puedes usar estos valores para probar:

- **Documento:** 1234567890
- **Nombre:** Juan Pérez
- **Celular:** 3001234567
- **Fecha nacimiento:** 15/05/1985
- **Estado civil:** Casado
- **Personas a cargo:** 2
- **Nivel estudios:** Profesional
- **Ocupación:** Empleado administrativo
- **Tipo contrato:** Indefinido
- **Experiencia:** 10 años
- **Ingreso principal:** $3,000,000
- **Gastos mensuales:** $1,800,000
- **Monto solicitado:** $10,000,000
- **Plazo:** 24 meses

## 🔄 Solo Ejecutar la Web (Modelo Ya Entrenado)

Si ya ejecutaste el sistema una vez y solo quieres volver a iniciar la web:

```bash
iniciar_web.bat
```

## 🐛 Solución de Problemas Comunes

### Error: "No se pudo cargar el modelo"

**Solución:** Entrena el modelo primero
```bash
python scripts\entrenar_modelo.py
```

### Error: "ValueError: high <= 0"

**Solución:** Ya está corregido en la nueva versión. Asegúrate de usar el código actualizado.

### Error: "Module 'flask' not found"

**Solución:** Instala las dependencias
```bash
pip install -r requirements.txt
```

### Puerto 5000 ya está en uso

**Solución:** Edita `run.py` línea 13 y cambia el puerto:
```python
app.run(host='0.0.0.0', port=8080, debug=True)
```

## 📊 Archivos Generados

Después de ejecutar todo, tendrás:

```
loan-ai-system/
├── data/
│   └── datos_prestamos.csv          (Datos de entrenamiento)
├── models/
│   ├── modelo_prestamos_final.h5    (Red neuronal entrenada)
│   ├── preprocessor.pkl             (Preprocesador)
│   └── metricas_modelo.json         (Métricas de evaluación)
└── [otros archivos...]
```

## 💡 Consejos

1. **Primera vez:** Usa `iniciar_sistema.bat` para configurar todo
2. **Desarrollo:** Usa `iniciar_web.bat` para lanzar solo la aplicación
3. **Re-entrenar:** Elimina los archivos en `models/` y ejecuta de nuevo el entrenamiento
4. **Nuevos datos:** Ejecuta `generar_datos_dummy.py` para crear nuevo dataset

## 🎉 ¡Listo!

Tu sistema de análisis de préstamos con IA está funcionando. Accede a http://localhost:5000 y comienza a evaluar solicitudes.

---

Para más información, consulta el [README.md](README.md)
