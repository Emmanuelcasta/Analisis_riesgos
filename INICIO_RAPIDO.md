# 🚀 Guía de Inicio Rápido# 🚀 Guía de Inicio Rápido# Guía de Uso Rápido



## ⚡ Opción 1: Ejecutar Todo Automáticamente (RECOMENDADO)



Simplemente ejecuta:## ⚡ Opción 1: Ejecutar Todo Automáticamente (RECOMENDADO)## Opción 1: Ejecutar Todo Automáticamente



```bash

.\iniciar_sistema.bat

```Simplemente ejecuta:Ejecuta este comando en PowerShell:



Este script realiza automáticamente:

1. ✅ Generación de 10,000 datos de entrenamiento

2. ✅ Entrenamiento del modelo de IA```bash```powershell

3. ✅ Pruebas de verificación

4. ✅ Lanzamiento de la aplicación web en http://localhost:5000iniciar_sistema.batcd C:\loan-ai-system



## 🔧 Opción 2: Ejecutar Paso por Paso```.\ejecutar_todo.bat



### 1. Instalar Dependencias```



```bashEste script realiza automáticamente:

.\instalar_dependencias.bat

```1. ✅ Generación de 10,000 datos de entrenamientoEste script ejecutará automáticamente:



O manualmente con el entorno virtual activado:2. ✅ Entrenamiento del modelo de IA1. ✅ Generación de datos dummy



```bash3. ✅ Pruebas de verificación2. ✅ Entrenamiento del modelo

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt4. ✅ Lanzamiento de la aplicación web en http://localhost:50003. ✅ Pruebas de verificación

```

4. ✅ Lanzamiento de la interfaz web

### 2. Generar Datos de Entrenamiento

## 🔧 Opción 2: Ejecutar Paso por Paso

```bash

python scripts\generar_datos_dummy.py## Opción 2: Ejecutar Paso por Paso

```

### 1. Instalar Dependencias

Crea: `data/datos_prestamos.csv` (10,000 registros)

### 1. Instalar dependencias

### 3. Entrenar el Modelo

```bash

```bash

python scripts\entrenar_modelo.pyinstalar_dependencias.bat```powershell

```

```pip install -r requirements.txt

Genera:

- `models/modelo_prestamos_final.h5````

- `models/preprocessor.pkl`

- `models/metricas_modelo.json`O manualmente:



### 4. Probar el Modelo### 2. Generar datos



```bash```bash

python scripts\probar_modelo.py

```pip install -r requirements.txt```powershell



### 5. Iniciar la Aplicación Web```python generar_datos_dummy.py



```bash```

.\iniciar_web.bat

```### 2. Generar Datos de Entrenamiento



O con Python:### 3. Entrenar modelo



```bash```bash

python run.py

```python scripts\generar_datos_dummy.py```powershell



Accede a: **http://localhost:5000**```python entrenar_modelo.py



## ⏱️ Tiempos Estimados```



| Paso | Tiempo |Crea: `data/datos_prestamos.csv` (10,000 registros)

|------|--------|

| Instalación de dependencias | 3-10 minutos |### 4. Probar modelo

| Generación de datos | 30-60 segundos |

| Entrenamiento del modelo | 3-5 minutos |### 3. Entrenar el Modelo

| Pruebas | 10-20 segundos |

| Inicio de la web | 5-10 segundos |```powershell



**Total:** ~15 minutos aproximadamente```bashpython probar_modelo.py



## 🌐 Uso de la Aplicación Webpython scripts\entrenar_modelo.py```



1. Abre tu navegador en http://localhost:5000```

2. Completa el formulario de solicitud de préstamo

3. Haz clic en "Analizar Solicitud"### 5. Iniciar interfaz web

4. Revisa los resultados:

   - Probabilidad de aprobaciónGenera:

   - Decisión (Aprobado/Rechazado)

   - Nivel de riesgo- `models/modelo_prestamos_final.h5````powershell

   - Análisis financiero detallado

   - Recomendaciones personalizadas- `models/preprocessor.pkl`streamlit run app_streamlit.py



## 📝 Estructura del Formulario- `models/metricas_modelo.json````



### Paso 1: Datos Generales

- Información personal (nombre, documento, contacto)

- Fecha de nacimiento### 4. Probar el Modelo## ⏱️ Tiempos Estimados

- Dirección y residencia



### Paso 2: Información Personal y Laboral

- Estado civil y dependientes```bash- Generación de datos: ~30 segundos

- Nivel educativo

- Ocupación y tipo de contratopython scripts\probar_modelo.py- Entrenamiento del modelo: ~3-5 minutos

- Sector económico y experiencia

```- Pruebas: ~10 segundos

### Paso 3: Información Financiera

- Ingresos mensuales (principal y adicionales)- Inicio de interfaz: ~5 segundos

- Gastos mensuales

- Monto del préstamo solicitado### 5. Iniciar la Aplicación Web

- Plazo en meses

- Línea de crédito## 🌐 Acceder a la Aplicación



## 🎯 Ejemplo de Datos de Prueba```bash



Puedes usar estos valores para probar:iniciar_web.batUna vez iniciada, abre tu navegador en:



- **Documento:** 1234567890```

- **Nombre:** Juan Pérez

- **Celular:** 3001234567**http://localhost:8501**

- **Fecha nacimiento:** 15/05/1985

- **Estado civil:** CasadoO con Python:

- **Personas a cargo:** 2

- **Nivel estudios:** Profesional## ❓ Solución de Problemas

- **Ocupación:** Empleado administrativo

- **Tipo contrato:** Indefinido```bash

- **Experiencia:** 10 años

- **Ingreso principal:** $3,000,000python run.py### Error: "No module named 'tensorflow'"

- **Gastos mensuales:** $1,800,000

- **Monto solicitado:** $10,000,000```

- **Plazo:** 24 meses

```powershell

## 🔄 Solo Ejecutar la Web (Modelo Ya Entrenado)

Accede a: **http://localhost:5000**pip install tensorflow==2.15.0

Si ya ejecutaste el sistema una vez y solo quieres volver a iniciar la web:

```

```bash

.\iniciar_web.bat## ⏱️ Tiempos Estimados

```

### Error: "No module named 'streamlit'"

## 🐛 Solución de Problemas Comunes

| Paso | Tiempo |

### Error: "No se pudo cargar el modelo"

|------|--------|```powershell

**Solución:** Entrena el modelo primero

```bash| Instalación de dependencias | 2-5 minutos |pip install streamlit

python scripts\entrenar_modelo.py

```| Generación de datos | 30-60 segundos |```



### Error: "Module 'flask' not found"| Entrenamiento del modelo | 3-5 minutos |



**Solución:** Activa el entorno virtual e instala las dependencias| Pruebas | 10-20 segundos |### Error: "Model file not found"

```bash

.\venv\Scripts\Activate.ps1| Inicio de la web | 5-10 segundos |

pip install -r requirements.txt

```Asegúrate de haber ejecutado primero:



### Puerto 5000 ya está en uso**Total:** ~10 minutos aproximadamente



**Solución:** Edita `run.py` línea 13 y cambia el puerto:```powershell

```python

app.run(host='0.0.0.0', port=8080, debug=True)## 🌐 Uso de la Aplicación Webpython entrenar_modelo.py

```

```

Luego accede a http://localhost:8080

1. Abre tu navegador en http://localhost:5000

## 📊 Archivos Generados

2. Completa el formulario de solicitud de préstamo## 📧 Soporte

Después de ejecutar todo, tendrás:

3. Haz clic en "Analizar Solicitud"

```

loan-ai-system/4. Revisa los resultados:Si encuentras problemas, revisa el archivo `README.md` completo para más detalles.

├── data/

│   └── datos_prestamos.csv          (Datos de entrenamiento)   - Probabilidad de aprobación

├── models/   - Decisión (Aprobado/Rechazado)

│   ├── modelo_prestamos_final.h5    (Red neuronal entrenada)   - Nivel de riesgo

│   ├── preprocessor.pkl             (Preprocesador)   - Análisis financiero detallado

│   └── metricas_modelo.json         (Métricas de evaluación)   - Recomendaciones personalizadas

└── venv/                            (Entorno virtual)

```## 📝 Estructura del Formulario



## 💡 Consejos### Paso 1: Datos Generales

- Información personal (nombre, documento, contacto)

1. **Primera vez:** Usa `.\iniciar_sistema.bat` para configurar todo- Fecha de nacimiento

2. **Desarrollo:** Usa `.\iniciar_web.bat` para lanzar solo la aplicación- Dirección y residencia

3. **Re-entrenar:** Elimina los archivos en `models/` y ejecuta de nuevo el entrenamiento

4. **Nuevos datos:** Ejecuta `python scripts\generar_datos_dummy.py` para crear nuevo dataset### Paso 2: Información Personal y Laboral

5. **Entorno virtual:** Siempre activa el entorno con `.\venv\Scripts\Activate.ps1` antes de ejecutar comandos Python- Estado civil y dependientes

- Nivel educativo

## 🎉 ¡Listo!- Ocupación y tipo de contrato

- Sector económico y experiencia

Tu sistema de análisis de préstamos con IA está funcionando. Accede a http://localhost:5000 y comienza a evaluar solicitudes.

### Paso 3: Información Financiera

---- Ingresos mensuales (principal y adicionales)

- Gastos mensuales

Para más información, consulta el [README.md](README.md)- Monto del préstamo solicitado

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
