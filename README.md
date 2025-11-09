# 🏦 Sistema de Análisis de Préstamos con IA

Sistema inteligente de evaluación de solicitudes de crédito usando **Deep Learning** y **Flask**.

---

## 📋 Descripción

Sistema que resuelve el problema de **inclusión financiera** para comunidades con bajos ingresos evaluando solicitudes de préstamo mediante inteligencia artificial, considerando múltiples factores más allá del historial crediticio tradicional.

### 🎯 Características Principales

- ✅ Evaluación automatizada de solicitudes de crédito
- ✅ Deep Learning con redes neuronales (91.50% accuracy)
- ✅ Procesamiento de texto con NLP
- ✅ Cálculo realista de cuotas con tasas de interés por producto
- ✅ 8 reglas de negocio estrictas para aprobación
- ✅ Interfaz web intuitiva con Flask
- ✅ Generación de datos sintéticos para entrenamiento

---

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Git

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/Emmanuelcasta/Analisis_riesgos.git
cd Analisis_riesgos
```

### 2️⃣ Crear Entorno Virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Dependencias principales:**
- Flask 3.0
- TensorFlow >=2.16.0
- NumPy >=1.26.0
- Pandas >=2.1.0
- Scikit-learn >=1.3.0
- Faker >=19.12.0

### 4️⃣ Generar Datos y Entrenar Modelo

**Generar datos sintéticos (10,000 registros):**
```bash
python scripts/generar_datos_dummy.py
```

**Entrenar el modelo:**
```bash
python scripts/entrenar_modelo.py
```

Esto generará:
- `data/datos_prestamos.csv` - Dataset de entrenamiento
- `models/modelo_prestamos_final.h5` - Modelo entrenado
- `models/preprocessor.pkl` - Preprocesador NLP
- `models/metricas_modelo.json` - Métricas del modelo
- `rendimiento_modelo.png` - Gráficas de rendimiento

### 5️⃣ Ejecutar la Aplicación Web

```bash
python run.py
```

La aplicación estará disponible en: **http://localhost:5000**

---

## 📁 Estructura del Proyecto

```
loan-ai-system/
├── app/                          # Aplicación web Flask
│   ├── __init__.py              # Inicialización de Flask
│   ├── routes.py                # Rutas y lógica de negocio
│   ├── static/                  # Archivos estáticos
│   │   ├── css/styles.css       # Estilos CSS
│   │   └── js/main.js           # JavaScript
│   └── templates/               # Templates HTML
│       ├── index.html           # Formulario de solicitud
│       ├── resultado.html       # Página de resultados
│       └── error.html           # Página de error
├── scripts/                     # Scripts de procesamiento
│   ├── generar_datos_dummy.py   # Generador de datos
│   ├── entrenar_modelo.py       # Entrenamiento del modelo
│   └── probar_modelo.py         # Pruebas del modelo
├── models/                      # Modelos entrenados
│   ├── modelo_prestamos_final.h5
│   ├── preprocessor.pkl
│   └── metricas_modelo.json
├── data/                        # Datos de entrenamiento
│   └── datos_prestamos.csv
├── docs/                        # Documentación
│   └── REGLAS_NEGOCIO.md       # Reglas de negocio detalladas
├── run.py                       # Punto de entrada
├── requirements.txt             # Dependencias
└── README.md                    # Este archivo
```

---

## 💰 Cálculo de Cuotas

El sistema utiliza **fórmula de amortización francesa** con tasas de interés realistas:

| Línea de Crédito | Tasa Mensual | Tasa EA |
|------------------|--------------|---------|
| Consumo | 2.5% | ~30% |
| Libre Inversión | 2.2% | ~26% |
| Vehículo | 1.8% | ~22% |
| Vivienda | 1.0% | ~12% |
| Microcrédito | 3.0% | ~36% |

**Fórmula:**
```
Cuota = Monto × [i × (1 + i)^n] / [(1 + i)^n - 1]
```

---

## 📊 Reglas de Negocio

### Criterios de Rechazo Automático

1. ❌ Gastos > 60% de ingresos
2. ❌ Ratio de endeudamiento > 40%
3. ❌ Capacidad de pago < 1.5x la cuota
4. ❌ Capacidad de pago negativa
5. ❌ Edad fuera de rango (20-65 años)
6. ❌ Ingresos insuficientes para el monto
7. ❌ Contratos inestables con poca antigüedad
8. ❌ Demasiadas personas a cargo con ingresos bajos

### Sistema de Scoring (0-100 puntos)

- **Factor 1:** Ratio de Endeudamiento (30 pts)
- **Factor 2:** Capacidad de Pago vs Cuota (25 pts)
- **Factor 3:** Ratio Gastos/Ingresos (20 pts)
- **Factor 4:** Estabilidad Laboral (15 pts)
- **Factor 5:** Nivel de Ingresos (10 pts)

**Decisión Final:**
- Score ≥ 70: ✅ Aprobación
- Score 60-69: ⚠️ Zona gris (evaluación adicional)
- Score < 60: ❌ Rechazo

---

## 📈 Métricas del Modelo

- **Accuracy:** 91.50%
- **Precision:** 77.10%
- **Recall:** 74.51%
- **AUC-ROC:** 96.12%

**Distribución del dataset:**
- Rechazados: 82.1%
- Aprobados: 17.9%

---

## 🧪 Probar el Modelo

```bash
python scripts/probar_modelo.py
```

---

## 🛠️ Uso de la Aplicación Web

1. **Acceder a** http://localhost:5000
2. **Llenar el formulario** con los datos del solicitante:
   - Datos personales y de contacto
   - Información laboral
   - Datos financieros
   - Monto y plazo solicitado
3. **Enviar la solicitud**
4. **Ver resultado** con:
   - Decisión (Aprobado/Rechazado)
   - Score de riesgo
   - Detalles financieros
   - Motivo de rechazo (si aplica)

---

## 📚 Documentación Adicional

- [Reglas de Negocio Detalladas](docs/REGLAS_NEGOCIO.md)
- [Guía de Inicio Rápido](INICIO_RAPIDO.md)

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## 👥 Autor

**Emmanuel Castro**
- GitHub: [@Emmanuelcasta](https://github.com/Emmanuelcasta)

---

## 🙏 Agradecimientos

- TensorFlow/Keras por el framework de Deep Learning
- Flask por el framework web
- Faker por la generación de datos sintéticos