# 📂 Estructura del Proyecto

```
loan-ai-system/                         🏠 Directorio principal
│
├── 📁 app/                             Aplicación web Flask
│   ├── __init__.py                    Inicialización de Flask
│   ├── routes.py                      Rutas y lógica de negocio
│   │
│   ├── 📁 static/                     Archivos estáticos
│   │   ├── 📁 css/                    
│   │   │   └── styles.css             Estilos personalizados
│   │   └── 📁 js/
│   │       └── main.js                JavaScript del cliente
│   │
│   └── 📁 templates/                  Plantillas HTML
│       ├── base.html                  Plantilla base
│       ├── index.html                 Formulario principal
│       ├── resultado.html             Página de resultados
│       └── error.html                 Página de error
│
├── 📁 scripts/                         Scripts de procesamiento
│   ├── generar_datos_dummy.py         Genera datos de entrenamiento
│   ├── entrenar_modelo.py             Entrena el modelo de IA
│   └── probar_modelo.py               Prueba el modelo entrenado
│
├── 📁 models/                          Modelos entrenados (generados)
│   ├── modelo_prestamos_final.h5      Red neuronal (generado)
│   ├── preprocessor.pkl               Preprocesador (generado)
│   └── metricas_modelo.json           Métricas (generado)
│
├── 📁 data/                            Datos de entrenamiento (generados)
│   └── datos_prestamos.csv            Dataset (generado)
│
├── 📁 utils/                           Utilidades (para futuras expansiones)
│
├── 📁 legacy/                          Archivos antiguos (respaldo)
│   ├── app_streamlit.py               App Streamlit original
│   └── ejecutar_todo.bat              Script antiguo
│
├── 📄 run.py                           🚀 Ejecutar aplicación web
├── 📄 requirements.txt                 Dependencias Python
│
├── 📄 iniciar_sistema.bat              ⚡ Ejecutar sistema completo
├── 📄 iniciar_web.bat                  🌐 Solo iniciar web
├── 📄 instalar_dependencias.bat        📦 Instalar dependencias
│
├── 📄 README.md                        📖 Documentación principal
├── 📄 INICIO_RAPIDO.md                 🚀 Guía de inicio rápido
├── 📄 INSTALACION.md                   🔧 Guía de instalación
│
└── 📄 .gitignore                       Git ignore file
```

## 📝 Descripción de Archivos Clave

### 🎯 Archivos de Ejecución

| Archivo | Descripción | Cuándo usar |
|---------|-------------|-------------|
| `iniciar_sistema.bat` | Ejecuta todo el flujo completo | Primera vez o re-entrenar |
| `iniciar_web.bat` | Solo inicia la aplicación web | Uso diario |
| `instalar_dependencias.bat` | Instala las dependencias Python | Solo una vez |

### 🐍 Scripts Python

| Script | Función | Salida |
|--------|---------|--------|
| `generar_datos_dummy.py` | Genera 10,000 registros de prueba | `data/datos_prestamos.csv` |
| `entrenar_modelo.py` | Entrena la red neuronal | Archivos en `models/` |
| `probar_modelo.py` | Valida el modelo entrenado | Imprime métricas en consola |
| `run.py` | Inicia el servidor Flask | Aplicación web en puerto 5000 |

### 🌐 Aplicación Web

| Archivo | Propósito |
|---------|-----------|
| `app/__init__.py` | Configuración y factory de Flask |
| `app/routes.py` | Rutas, endpoints y lógica de predicción |
| `app/templates/index.html` | Formulario de solicitud (3 pasos) |
| `app/templates/resultado.html` | Página de resultados con análisis |
| `app/static/css/styles.css` | Estilos personalizados |
| `app/static/js/main.js` | Validaciones y funciones JS |

### 🤖 Modelos y Datos (Generados)

| Archivo | Tamaño aprox. | Descripción |
|---------|---------------|-------------|
| `models/modelo_prestamos_final.h5` | 50-100 MB | Red neuronal entrenada |
| `models/preprocessor.pkl` | 5-10 MB | Preprocesador de datos |
| `models/metricas_modelo.json` | 2 KB | Métricas de evaluación |
| `data/datos_prestamos.csv` | 10-15 MB | Dataset de entrenamiento |

## 🔄 Flujo del Sistema

```
1. Usuario accede a http://localhost:5000
   ↓
2. Flask carga index.html (formulario)
   ↓
3. Usuario completa formulario
   ↓
4. POST a /analizar
   ↓
5. routes.py procesa datos
   ↓
6. Modelo hace predicción
   ↓
7. Flask renderiza resultado.html
   ↓
8. Usuario ve análisis completo
```

## 🎨 Tecnologías por Carpeta

### `/app` - Frontend & Backend Web
- **Flask 3.0** - Framework web
- **Bootstrap 5** - UI/UX
- **Chart.js** - Gráficos interactivos
- **Jinja2** - Templates

### `/scripts` - Machine Learning
- **TensorFlow/Keras** - Deep Learning
- **Pandas** - Manipulación de datos
- **NumPy** - Operaciones numéricas
- **Scikit-learn** - Preprocessing
- **Faker** - Generación de datos

### `/models` - Modelos Entrenados
- **H5 Format** - Keras models
- **Pickle** - Python objects
- **JSON** - Configuración

## 📊 Tamaños Aproximados

```
Total del proyecto: ~200-300 MB (con modelos)
├── Sin modelos: ~5 MB (código fuente)
├── Con modelos: ~150-250 MB (después de entrenar)
└── Con datos: ~10-15 MB (datos de entrenamiento)
```

## 🗂️ Archivos Ignorados por Git

Los siguientes archivos NO se suben al repositorio:

- `models/*.h5` - Modelos entrenados (muy grandes)
- `models/*.pkl` - Preprocesadores
- `data/*.csv` - Datos generados
- `__pycache__/` - Cache de Python
- `.vscode/` - Configuración de editor

Estos se generan localmente al ejecutar `iniciar_sistema.bat`

## 🔐 Archivos de Configuración

| Archivo | Propósito |
|---------|-----------|
| `requirements.txt` | Dependencias Python y versiones |
| `.gitignore` | Archivos excluidos de Git |
| `app/__init__.py` | Configuración de Flask |

## 📚 Documentación

| Documento | Para quién |
|-----------|-----------|
| `README.md` | Visión general y features |
| `INICIO_RAPIDO.md` | Usuarios nuevos |
| `INSTALACION.md` | Guía de instalación detallada |
| Este archivo | Desarrolladores |

## 🎯 Próximas Expansiones

Carpetas preparadas para crecer:

```
├── 📁 utils/              → Funciones auxiliares
├── 📁 tests/              → Tests unitarios (futuro)
├── 📁 config/             → Archivos de configuración (futuro)
└── 📁 logs/               → Logs de la aplicación (futuro)
```

---

**Estructura limpia y organizada siguiendo mejores prácticas de Flask** ✨
