# 🚀 Guía de Inicio Rápido# 🚀 Guía de Inicio Rápido# 🚀 Guía de Inicio Rápido# Guía de Uso Rápido

## Sistema de Análisis de Riesgo Crediticio con IA



Esta guía te llevará desde la instalación hasta tener el sistema funcionando en **menos de 10 minutos**.

## ⚡ Opción 1: Ejecutar Todo Automáticamente (RECOMENDADO)

---



## 📋 Prerrequisitos

Simplemente ejecuta:## ⚡ Opción 1: Ejecutar Todo Automáticamente (RECOMENDADO)## Opción 1: Ejecutar Todo Automáticamente

Antes de comenzar, asegúrate de tener instalado:



- ✅ **Python 3.12 o superior** → [Descargar aquí](https://www.python.org/downloads/)

- ✅ **Git** → [Descargar aquí](https://git-scm.com/downloads)```bash

- ✅ **PowerShell** (Windows) o **Terminal** (Linux/Mac)

- ✅ **8GB RAM mínimo** (para entrenamiento de modelos).\iniciar_sistema.bat

- ✅ **500MB espacio en disco**

```Simplemente ejecuta:Ejecuta este comando en PowerShell:

### Verificar instalación de Python



```bash

python --versionEste script realiza automáticamente:

# Debe mostrar: Python 3.12.x o superior

```1. ✅ Generación de 10,000 datos de entrenamiento



---2. ✅ Entrenamiento del modelo de IA```bash```powershell



## ⚡ Opción 1: Ejecución Automática (RECOMENDADA)3. ✅ Pruebas de verificación



### Windows4. ✅ Lanzamiento de la aplicación web en http://localhost:5000iniciar_sistema.batcd C:\loan-ai-system



```powershell

# 1. Abrir PowerShell en la carpeta del proyecto

cd C:\ruta\a\loan-ai-system## 🔧 Opción 2: Ejecutar Paso por Paso```.\ejecutar_todo.bat



# 2. Ejecutar script automático

.\ejecutar_todo.bat

```### 1. Instalar Dependencias```



### Linux/Mac



```bash```bashEste script realiza automáticamente:

# 1. Abrir terminal en la carpeta del proyecto

cd /ruta/a/loan-ai-system.\instalar_dependencias.bat



# 2. Dar permisos de ejecución```1. ✅ Generación de 10,000 datos de entrenamientoEste script ejecutará automáticamente:

chmod +x ejecutar_todo.sh



# 3. Ejecutar script automático

./ejecutar_todo.shO manualmente con el entorno virtual activado:2. ✅ Entrenamiento del modelo de IA1. ✅ Generación de datos dummy

```



### ¿Qué hace el script automático?

```bash3. ✅ Pruebas de verificación2. ✅ Entrenamiento del modelo

1. ✅ Crea entorno virtual Python

2. ✅ Instala todas las dependencias (Flask, TensorFlow, etc.).\venv\Scripts\Activate.ps1

3. ✅ Genera 10,000 registros sintéticos de datos

4. ✅ Entrena 3 modelos de Machine Learning:pip install -r requirements.txt4. ✅ Lanzamiento de la aplicación web en http://localhost:50003. ✅ Pruebas de verificación

   - Random Forest (98.35% accuracy)

   - Gradient Boosting (98.25% accuracy)```

   - Deep Learning (44.50% accuracy)

5. ✅ Selecciona automáticamente el mejor modelo4. ✅ Lanzamiento de la interfaz web

6. ✅ Inicia la aplicación web en http://localhost:5000

### 2. Generar Datos de Entrenamiento

**Tiempo estimado:** 5-8 minutos (depende de tu computadora)

## 🔧 Opción 2: Ejecutar Paso por Paso

---

```bash

## 🔧 Opción 2: Instalación Paso a Paso

python scripts\generar_datos_dummy.py## Opción 2: Ejecutar Paso por Paso

### Paso 1: Clonar el Repositorio

```

```bash

# Si aún no tienes el proyecto### 1. Instalar Dependencias

git clone https://github.com/Emmanuelcasta/Analisis_riesgos.git

cd Analisis_riesgosCrea: `data/datos_prestamos.csv` (10,000 registros)

```

### 1. Instalar dependencias

---

### 3. Entrenar el Modelo

### Paso 2: Crear Entorno Virtual

```bash

#### Windows (PowerShell)

```bash

```powershell

# Crear entorno virtualpython scripts\entrenar_modelo.pyinstalar_dependencias.bat```powershell

python -m venv venv

```

# Activar entorno virtual

.\venv\Scripts\Activate.ps1```pip install -r requirements.txt



# Si aparece error de permisos, ejecutar:Genera:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

```- `models/modelo_prestamos_final.h5````



#### Windows (CMD)- `models/preprocessor.pkl`



```cmd- `models/metricas_modelo.json`O manualmente:

# Crear entorno virtual

python -m venv venv



# Activar entorno virtual### 4. Probar el Modelo### 2. Generar datos

venv\Scripts\activate.bat

```



#### Linux/Mac```bash```bash



```bashpython scripts\probar_modelo.py

# Crear entorno virtual

python3 -m venv venv```pip install -r requirements.txt```powershell



# Activar entorno virtual

source venv/bin/activate

```### 5. Iniciar la Aplicación Web```python generar_datos_dummy.py



**✅ Verificación:** El prompt debe mostrar `(venv)` al inicio



---```bash```



### Paso 3: Instalar Dependencias.\iniciar_web.bat



```bash```### 2. Generar Datos de Entrenamiento

# Con el entorno virtual activado

pip install --upgrade pip

pip install -r requirements.txt

```O con Python:### 3. Entrenar modelo



**Tiempo estimado:** 2-3 minutos



**Dependencias principales instaladas:**```bash```bash

- Flask 3.0 (Web framework)

- TensorFlow 2.16.1 (Deep Learning)python run.py

- Scikit-learn 1.3.0+ (Random Forest, Gradient Boosting)

- Pandas 2.1.0+ (Manipulación de datos)```python scripts\generar_datos_dummy.py```powershell

- NumPy 1.26.0+ (Cálculos numéricos)

- Faker 19.12.0+ (Generación de datos sintéticos)



**✅ Verificación:**Accede a: **http://localhost:5000**```python entrenar_modelo.py



```bash

python -c "import flask; import tensorflow; import sklearn; print('✅ Todas las dependencias instaladas correctamente')"

```## ⏱️ Tiempos Estimados```



---



### Paso 4: Generar Datos de Entrenamiento| Paso | Tiempo |Crea: `data/datos_prestamos.csv` (10,000 registros)



```bash|------|--------|

python scripts/generar_datos_dummy.py

```| Instalación de dependencias | 3-10 minutos |### 4. Probar modelo



**Salida esperada:**| Generación de datos | 30-60 segundos |



```| Entrenamiento del modelo | 3-5 minutos |### 3. Entrenar el Modelo

🏦 GENERADOR DE DATOS SINTÉTICOS PARA PRÉSTAMOS

================================================| Pruebas | 10-20 segundos |

Generando 10,000 solicitudes de crédito...

  ✓ 2,000 registros generados| Inicio de la web | 5-10 segundos |```powershell

  ✓ 4,000 registros generados

  ✓ 6,000 registros generados

  ✓ 8,000 registros generados

  ✓ 10,000 registros generados**Total:** ~15 minutos aproximadamente```bashpython probar_modelo.py



✅ Dataset guardado en: data/datos_prestamos.csv



📊 Distribución:## 🌐 Uso de la Aplicación Webpython scripts\entrenar_modelo.py```

  - Aprobados: 1,790 (17.9%)

  - Rechazados: 8,210 (82.1%)

```

1. Abre tu navegador en http://localhost:5000```

**Tiempo estimado:** 30-60 segundos

2. Completa el formulario de solicitud de préstamo

**Archivo generado:** `data/datos_prestamos.csv` (10,000 registros)

3. Haz clic en "Analizar Solicitud"### 5. Iniciar interfaz web

---

4. Revisa los resultados:

### Paso 5: Entrenar Modelos de Machine Learning

   - Probabilidad de aprobaciónGenera:

```bash

python scripts/entrenar_modelos_comparativa.py   - Decisión (Aprobado/Rechazado)

```

   - Nivel de riesgo- `models/modelo_prestamos_final.h5````powershell

**Salida esperada:**

   - Análisis financiero detallado

```

🚀 ENTRENAMIENTO COMPARATIVO DE MODELOS   - Recomendaciones personalizadas- `models/preprocessor.pkl`streamlit run app_streamlit.py

======================================

Modelos a entrenar:

  1. Deep Learning (Red Neuronal Profunda)

  2. Random Forest Classifier## 📝 Estructura del Formulario- `models/metricas_modelo.json````

  3. Gradient Boosting Classifier



📂 Cargando datos...

   ✓ Cargados 10,000 registros### Paso 1: Datos Generales



🔧 Preparando datos...- Información personal (nombre, documento, contacto)

   ✓ Features: 42 variables

   ✓ Train: 8,000 muestras- Fecha de nacimiento### 4. Probar el Modelo## ⏱️ Tiempos Estimados

   ✓ Test: 2,000 muestras

- Dirección y residencia

==================================================================

🧠 MODELO 1: DEEP LEARNING

==================================================================

   ✓ Arquitectura: 56,065 parámetros### Paso 2: Información Personal y Laboral

   ⏳ Entrenando (max 100 épocas)...

   ✅ Entrenamiento completado en 44.11s- Estado civil y dependientes```bash- Generación de datos: ~30 segundos

   📊 Accuracy: 44.50%

   📊 AUC-ROC: 0.6765- Nivel educativo



==================================================================- Ocupación y tipo de contratopython scripts\probar_modelo.py- Entrenamiento del modelo: ~3-5 minutos

🌲 MODELO 2: RANDOM FOREST

==================================================================- Sector económico y experiencia

   ✓ Configuración: 200 árboles

   ⏳ Entrenando...```- Pruebas: ~10 segundos

   ✅ Entrenamiento completado en 0.35s

   📊 Accuracy: 98.35%### Paso 3: Información Financiera

   📊 AUC-ROC: 0.9992

- Ingresos mensuales (principal y adicionales)- Inicio de interfaz: ~5 segundos

==================================================================

⚡ MODELO 3: GRADIENT BOOSTING- Gastos mensuales

==================================================================

   ✓ Configuración: 200 estimadores- Monto del préstamo solicitado### 5. Iniciar la Aplicación Web

   ⏳ Entrenando...

   ✅ Entrenamiento completado en 9.66s- Plazo en meses

   📊 Accuracy: 98.25%

   📊 AUC-ROC: 0.9991- Línea de crédito## 🌐 Acceder a la Aplicación



📊 TABLA COMPARATIVA

======================================

Modelo                  Accuracy    AUC-ROC    Train(s)## 🎯 Ejemplo de Datos de Prueba```bash

------------------------------------------------------

Random Forest           98.35%      0.9992     0.35

Gradient Boosting       98.25%      0.9991     9.66

Deep Learning           44.50%      0.6765     44.11Puedes usar estos valores para probar:iniciar_web.batUna vez iniciada, abre tu navegador en:



🏆 MEJOR MODELO: Random Forest



💾 Guardando modelos...- **Documento:** 1234567890```

   ✓ Random Forest: models/modelo_random_forest.pkl

   ✓ Gradient Boosting: models/modelo_gradient_boosting.pkl- **Nombre:** Juan Pérez

   ✓ Deep Learning: models/modelo_deep_learning.h5

   ✓ Preprocessor: models/preprocessor_comparativa.pkl- **Celular:** 3001234567**http://localhost:8501**



✅ PROCESO COMPLETADO EXITOSAMENTE- **Fecha nacimiento:** 15/05/1985

```

- **Estado civil:** CasadoO con Python:

**Tiempo estimado:** 1-2 minutos

- **Personas a cargo:** 2

**Archivos generados:**

- **Nivel estudios:** Profesional## ❓ Solución de Problemas

- `models/modelo_random_forest.pkl` → Mejor modelo (98.35%)

- `models/modelo_gradient_boosting.pkl` → Segundo lugar- **Ocupación:** Empleado administrativo

- `models/modelo_deep_learning.h5` → Deep Learning

- `models/preprocessor_comparativa.pkl` → Preprocesador- **Tipo contrato:** Indefinido```bash

- `models/comparativa_modelos.json` → Métricas detalladas

- `models/comparativa_modelos.csv` → Tabla comparativa- **Experiencia:** 10 años

- `models/modelo_config.json` → Configuración de producción

- **Ingreso principal:** $3,000,000python run.py### Error: "No module named 'tensorflow'"

---

- **Gastos mensuales:** $1,800,000

### Paso 6: Ejecutar la Aplicación Web

- **Monto solicitado:** $10,000,000```

```bash

python run.py- **Plazo:** 24 meses

```

```powershell

**Salida esperada:**

## 🔄 Solo Ejecutar la Web (Modelo Ya Entrenado)

```

============================================================Accede a: **http://localhost:5000**pip install tensorflow==2.15.0

Sistema de Análisis de Préstamos con IA

============================================================Si ya ejecutaste el sistema una vez y solo quieres volver a iniciar la web:



Iniciando servidor web...```

Accede a: http://localhost:5000

```bash

Presiona Ctrl+C para detener el servidor

.\iniciar_web.bat## ⏱️ Tiempos Estimados

 * Serving Flask app 'app'

 * Debug mode: on```

 * Running on http://127.0.0.1:5000

### Error: "No module named 'streamlit'"

📊 Cargando modelo: Random Forest

✅ Modelo Random Forest cargado (Accuracy: 98.35%)## 🐛 Solución de Problemas Comunes

```

| Paso | Tiempo |

**✅ Listo!** Abre tu navegador en: **http://localhost:5000**

### Error: "No se pudo cargar el modelo"

---

|------|--------|```powershell

## 🌐 Uso de la Aplicación Web

**Solución:** Entrena el modelo primero

### Página Principal

```bash| Instalación de dependencias | 2-5 minutos |pip install streamlit

![Formulario de solicitud](https://via.placeholder.com/800x400/4CAF50/FFFFFF?text=Formulario+de+Solicitud)

python scripts\entrenar_modelo.py

1. **Paso 1: Datos Generales**

   - Tipo y número de documento```| Generación de datos | 30-60 segundos |```

   - Nombres y apellidos

   - Contacto (celular, email)

   - Residencia (departamento, ciudad, dirección)

### Error: "Module 'flask' not found"| Entrenamiento del modelo | 3-5 minutos |

2. **Paso 2: Conocimiento del Cliente**

   - Estado civil

   - Personas a cargo

   - Ocupación y sector económico**Solución:** Activa el entorno virtual e instala las dependencias| Pruebas | 10-20 segundos |### Error: "Model file not found"

   - Tipo de contrato

   - Antigüedad laboral```bash

   - Nivel de estudios

.\venv\Scripts\Activate.ps1| Inicio de la web | 5-10 segundos |

3. **Paso 3: Información Financiera**

   - Ingresos principales y adicionalespip install -r requirements.txt

   - Gastos mensuales

   - **Monto solicitado**```Asegúrate de haber ejecutado primero:

   - **Plazo en meses**

   - Línea de crédito



### Resultado de la Evaluación### Puerto 5000 ya está en uso**Total:** ~10 minutos aproximadamente



Después de enviar el formulario, verás:



#### ✅ Si es APROBADO:**Solución:** Edita `run.py` línea 13 y cambia el puerto:```powershell



``````python

╔═══════════════════════════════════════╗

║     ✅ SOLICITUD APROBADA             ║app.run(host='0.0.0.0', port=8080, debug=True)## 🌐 Uso de la Aplicación Webpython entrenar_modelo.py

╚═══════════════════════════════════════╝

```

Probabilidad de aprobación: 88%

Nivel de riesgo: BAJO```



💰 Detalles Financieros:Luego accede a http://localhost:8080

  • Monto aprobado: $5,000,000

  • Plazo: 24 meses1. Abre tu navegador en http://localhost:5000

  • Tasa de interés: 30% EA (2.5% mensual)

  • Cuota mensual: $250,000## 📊 Archivos Generados

  • Capacidad de pago: $1,200,000

  • Ratio de endeudamiento: 10%2. Completa el formulario de solicitud de préstamo## 📧 Soporte



✨ Este perfil cumple con todos los criterios de aprobaciónDespués de ejecutar todo, tendrás:

```

3. Haz clic en "Analizar Solicitud"

#### ❌ Si es RECHAZADO:

```

```

╔═══════════════════════════════════════╗loan-ai-system/4. Revisa los resultados:Si encuentras problemas, revisa el archivo `README.md` completo para más detalles.

║     ❌ SOLICITUD RECHAZADA            ║

╚═══════════════════════════════════════╝├── data/



Probabilidad de aprobación: 23%│   └── datos_prestamos.csv          (Datos de entrenamiento)   - Probabilidad de aprobación

Nivel de riesgo: ALTO

├── models/   - Decisión (Aprobado/Rechazado)

⚠️ Motivos de rechazo:

  1. Gastos exceden 60% de los ingresos│   ├── modelo_prestamos_final.h5    (Red neuronal entrenada)   - Nivel de riesgo

  2. Ratio de endeudamiento excede 40%

  3. Capacidad de pago insuficiente│   ├── preprocessor.pkl             (Preprocesador)   - Análisis financiero detallado



💡 Recomendaciones:│   └── metricas_modelo.json         (Métricas de evaluación)   - Recomendaciones personalizadas

  • Reducir el monto solicitado

  • Aumentar el plazo para disminuir la cuota└── venv/                            (Entorno virtual)

  • Mejorar la capacidad de pago antes de solicitar

``````## 📝 Estructura del Formulario



---



## 🧪 Probar con Datos de Ejemplo## 💡 Consejos### Paso 1: Datos Generales



### Caso 1: Perfil APROBADO- Información personal (nombre, documento, contacto)



```1. **Primera vez:** Usa `.\iniciar_sistema.bat` para configurar todo- Fecha de nacimiento

Tipo documento: Cédula de Ciudadanía

Documento: 12345678902. **Desarrollo:** Usa `.\iniciar_web.bat` para lanzar solo la aplicación- Dirección y residencia

Nombres: Juan Carlos

Apellidos: Pérez Gómez3. **Re-entrenar:** Elimina los archivos en `models/` y ejecuta de nuevo el entrenamiento

Celular: 3001234567

Email: juan.perez@email.com4. **Nuevos datos:** Ejecuta `python scripts\generar_datos_dummy.py` para crear nuevo dataset### Paso 2: Información Personal y Laboral



Departamento: Cundinamarca5. **Entorno virtual:** Siempre activa el entorno con `.\venv\Scripts\Activate.ps1` antes de ejecutar comandos Python- Estado civil y dependientes

Ciudad: Bogotá

Dirección: Calle 100 # 20-30- Nivel educativo



Estado civil: Casado## 🎉 ¡Listo!- Ocupación y tipo de contrato

Personas a cargo: 2

Género: Masculino- Sector económico y experiencia

Ocupación: Empleado administrativo

Tipo contrato: IndefinidoTu sistema de análisis de préstamos con IA está funcionando. Accede a http://localhost:5000 y comienza a evaluar solicitudes.

Antigüedad: 5 años

Nivel estudios: Profesional### Paso 3: Información Financiera



Ingreso principal: $4,000,000---- Ingresos mensuales (principal y adicionales)

Otros ingresos: $500,000

Gastos mensuales: $2,000,000- Gastos mensuales

Monto solicitado: $8,000,000

Plazo: 36 mesesPara más información, consulta el [README.md](README.md)- Monto del préstamo solicitado

Línea crédito: Consumo

```- Plazo en meses

- Línea de crédito

**Resultado esperado:** ✅ APROBADO (Probabilidad ~85%)

## 🎯 Ejemplo de Datos de Prueba

---

Puedes usar estos valores para probar:

### Caso 2: Perfil RECHAZADO

- **Documento:** 1234567890

```- **Nombre:** Juan Pérez

Tipo documento: Cédula de Ciudadanía- **Celular:** 3001234567

Documento: 9876543210- **Fecha nacimiento:** 15/05/1985

Nombres: María Fernanda- **Estado civil:** Casado

Apellidos: López Castro- **Personas a cargo:** 2

Celular: 3109876543- **Nivel estudios:** Profesional

Email: maria.lopez@email.com- **Ocupación:** Empleado administrativo

- **Tipo contrato:** Indefinido

Departamento: Atlántico- **Experiencia:** 10 años

Ciudad: Barranquilla- **Ingreso principal:** $3,000,000

Dirección: Carrera 50 # 80-15- **Gastos mensuales:** $1,800,000

- **Monto solicitado:** $10,000,000

Estado civil: Soltera- **Plazo:** 24 meses

Personas a cargo: 5

Género: Femenino## 🔄 Solo Ejecutar la Web (Modelo Ya Entrenado)

Ocupación: Independiente

Tipo contrato: IndependienteSi ya ejecutaste el sistema una vez y solo quieres volver a iniciar la web:

Antigüedad: 6 meses

Nivel estudios: Bachillerato```bash

iniciar_web.bat

Ingreso principal: $1,500,000```

Otros ingresos: $0

Gastos mensuales: $1,300,000## 🐛 Solución de Problemas Comunes

Monto solicitado: $10,000,000

Plazo: 12 meses### Error: "No se pudo cargar el modelo"

Línea crédito: Microcrédito

```**Solución:** Entrena el modelo primero

```bash

**Resultado esperado:** ❌ RECHAZADO (Múltiples criterios incumplidos)python scripts\entrenar_modelo.py

```

---

### Error: "ValueError: high <= 0"

## 🛑 Detener la Aplicación

**Solución:** Ya está corregido en la nueva versión. Asegúrate de usar el código actualizado.

Para detener el servidor web, presiona:

### Error: "Module 'flask' not found"

**Windows/Linux/Mac:** `Ctrl + C`

**Solución:** Instala las dependencias

---```bash

pip install -r requirements.txt

## 🔄 Volver a Entrenar con Nuevos Datos```



Si quieres regenerar los datos o volver a entrenar:### Puerto 5000 ya está en uso



```bash**Solución:** Edita `run.py` línea 13 y cambia el puerto:

# 1. Generar nuevos datos (opcional)```python

python scripts/generar_datos_dummy.pyapp.run(host='0.0.0.0', port=8080, debug=True)

```

# 2. Entrenar modelos de nuevo

python scripts/entrenar_modelos_comparativa.py## 📊 Archivos Generados



# 3. Reiniciar aplicaciónDespués de ejecutar todo, tendrás:

python run.py

``````

loan-ai-system/

---├── data/

│   └── datos_prestamos.csv          (Datos de entrenamiento)

## ❓ Solución de Problemas Comunes├── models/

│   ├── modelo_prestamos_final.h5    (Red neuronal entrenada)

### Error: "ModuleNotFoundError: No module named 'flask'"│   ├── preprocessor.pkl             (Preprocesador)

│   └── metricas_modelo.json         (Métricas de evaluación)

**Causa:** Entorno virtual no activado o dependencias no instaladas└── [otros archivos...]

```

**Solución:**

## 💡 Consejos

```bash

# Activar entorno virtual1. **Primera vez:** Usa `iniciar_sistema.bat` para configurar todo

source venv/bin/activate  # Linux/Mac2. **Desarrollo:** Usa `iniciar_web.bat` para lanzar solo la aplicación

# o: .\venv\Scripts\Activate.ps1  # Windows PowerShell3. **Re-entrenar:** Elimina los archivos en `models/` y ejecuta de nuevo el entrenamiento

4. **Nuevos datos:** Ejecuta `generar_datos_dummy.py` para crear nuevo dataset

# Reinstalar dependencias

pip install -r requirements.txt## 🎉 ¡Listo!

```

Tu sistema de análisis de préstamos con IA está funcionando. Accede a http://localhost:5000 y comienza a evaluar solicitudes.

---

---

### Error: "FileNotFoundError: datos_prestamos.csv"

Para más información, consulta el [README.md](README.md)

**Causa:** No se han generado los datos de entrenamiento

**Solución:**

```bash
python scripts/generar_datos_dummy.py
```

---

### Error: "Port 5000 already in use"

**Causa:** Otro proceso está usando el puerto 5000

**Solución:**

```bash
# Opción 1: Cambiar puerto (editar run.py)
# app.run(debug=True, port=5001)

# Opción 2: Matar proceso en puerto 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Opción 2: Matar proceso en puerto 5000 (Linux/Mac)
lsof -ti:5000 | xargs kill -9
```

---

### Error: "TensorFlow not found" o problemas con GPU

**Causa:** TensorFlow requiere configuración especial en algunos sistemas

**Solución:**

```bash
# Reinstalar TensorFlow (solo CPU, más compatible)
pip uninstall tensorflow
pip install tensorflow-cpu==2.16.1
```

---

### Error: "ExecutionPolicy" en PowerShell

**Causa:** Restricciones de seguridad de Windows

**Solución:**

```powershell
# Ejecutar como Administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# O usar CMD en lugar de PowerShell
venv\Scripts\activate.bat
```

---

## 📊 Verificar que Todo Funciona

### Test Rápido

```bash
# 1. Verificar que existe el dataset
dir data\datos_prestamos.csv  # Windows
# o: ls data/datos_prestamos.csv  # Linux/Mac

# 2. Verificar que existen los modelos
dir models\modelo_random_forest.pkl  # Windows
# o: ls models/modelo_random_forest.pkl  # Linux/Mac

# 3. Probar importaciones de Python
python -c "from app import create_app; print('✅ Aplicación OK')"

# 4. Verificar modelo se carga correctamente
python -c "import pickle; modelo = pickle.load(open('models/modelo_random_forest.pkl', 'rb')); print('✅ Modelo carga OK')"
```

---

## 📚 Próximos Pasos

Una vez que tengas el sistema funcionando:

1. 📖 Lee la [documentación completa](README.md)
2. 🔬 Revisa el [artículo científico](docs/Articulo_Cientifico_IEEE.md)
3. 📊 Analiza los [reportes de comparación](models/COMPARACION_MODELOS.md)
4. 🎯 Consulta los [objetivos cumplidos](OBJETIVOS_CUMPLIDOS.md)
5. 🚫 Entiende las [reglas de negocio](REGLAS_NEGOCIO.md)
6. 📋 Profundiza en la [especificación de la base de datos](ESPECIFICACION_BASE_DATOS.md)

---

## 💬 ¿Necesitas Ayuda?

- 🐛 **Reportar bugs:** [GitHub Issues](https://github.com/Emmanuelcasta/Analisis_riesgos/issues)
- 📧 **Contacto:** GitHub [@Emmanuelcasta](https://github.com/Emmanuelcasta)
- 📖 **Documentación:** Ver [README.md](README.md)

---

**🎉 ¡Felicitaciones! Ya tienes tu sistema de análisis crediticio funcionando.**

**⭐ Si esta guía te fue útil, considera darle una estrella al proyecto en GitHub!**
