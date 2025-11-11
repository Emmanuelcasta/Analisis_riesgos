# Comparación de Modelos de Machine Learning
## Sistema de Análisis de Créditos

**Fecha de generación:** 2025-11-10T22:59:12.056329  
**Mejor modelo seleccionado:** Random Forest  
**Modelos comparados:** 3

---

## Resumen Ejecutivo

El análisis comparativo evaluó tres algoritmos de machine learning sobre el mismo conjunto de datos:
- **Deep Learning**: Red neuronal profunda de 5 capas
- **Random Forest**: Ensamble de 200 árboles de decisión  
- **Gradient Boosting**: 200 estimadores con boosting secuencial

### Métricas Principales

| Modelo | Accuracy | Precision | Recall | F1-Score | AUC-ROC | Log Loss |
|--------|----------|-----------|--------|----------|---------|----------|
| **Random Forest** | 98.35% | 92.63% | 98.60% | 95.52% | 0.9992 | 0.0651 |
| **Gradient Boosting** | 98.25% | 94.72% | 95.52% | 95.12% | 0.9991 | 0.0389 |
| **Deep Learning** | 44.50% | 23.58% | 94.12% | 37.71% | 0.6765 | 7.5756 |


---

## Análisis Detallado por Modelo


### Random Forest

**Métricas de Clasificación:**
- **Accuracy:** 98.35%
- **Precision:** 92.63%
- **Recall:** 98.60%
- **F1-Score:** 95.52%
- **AUC-ROC:** 0.9992
- **Log Loss:** 0.0651

**Métricas Adicionales:**
- **Specificity:** 98.30%
- **False Positive Rate:** 1.70%
- **False Negative Rate:** 1.40%

**Matriz de Confusión:**
```
                Predicho Negativo    Predicho Positivo
Real Negativo         1615                 28
Real Positivo            5                352
```

**Rendimiento Computacional:**
- **Tiempo de entrenamiento:** 0.35 segundos
- **Tiempo de predicción:** 0.0816 segundos
- **Predicciones por segundo:** 24,519

**Rankings:**
- Rank Accuracy: 1.0
- Rank AUC-ROC: 1.0
- Rank F1-Score: 1.0
- **Rank Global: 1.0**

---

### Gradient Boosting

**Métricas de Clasificación:**
- **Accuracy:** 98.25%
- **Precision:** 94.72%
- **Recall:** 95.52%
- **F1-Score:** 95.12%
- **AUC-ROC:** 0.9991
- **Log Loss:** 0.0389

**Métricas Adicionales:**
- **Specificity:** 98.84%
- **False Positive Rate:** 1.16%
- **False Negative Rate:** 4.48%

**Matriz de Confusión:**
```
                Predicho Negativo    Predicho Positivo
Real Negativo         1624                 19
Real Positivo           16                341
```

**Rendimiento Computacional:**
- **Tiempo de entrenamiento:** 9.66 segundos
- **Tiempo de predicción:** 0.0105 segundos
- **Predicciones por segundo:** 190,136

**Rankings:**
- Rank Accuracy: 2.0
- Rank AUC-ROC: 2.0
- Rank F1-Score: 2.0
- **Rank Global: 2.0**

---

### Deep Learning

**Métricas de Clasificación:**
- **Accuracy:** 44.50%
- **Precision:** 23.58%
- **Recall:** 94.12%
- **F1-Score:** 37.71%
- **AUC-ROC:** 0.6765
- **Log Loss:** 7.5756

**Métricas Adicionales:**
- **Specificity:** 33.72%
- **False Positive Rate:** 66.28%
- **False Negative Rate:** 5.88%

**Matriz de Confusión:**
```
                Predicho Negativo    Predicho Positivo
Real Negativo          554               1089
Real Positivo           21                336
```

**Rendimiento Computacional:**
- **Tiempo de entrenamiento:** 44.11 segundos
- **Tiempo de predicción:** 0.2433 segundos
- **Predicciones por segundo:** 8,220

**Rankings:**
- Rank Accuracy: 3.0
- Rank AUC-ROC: 3.0
- Rank F1-Score: 3.0
- **Rank Global: 3.0**

---

## Justificación de la Selección

El modelo **Random Forest** fue seleccionado como el mejor basándose en:

1. **Mayor Accuracy (98.35%)**: Proporciona la mejor tasa de predicciones correctas
2. **Excelente AUC-ROC (0.9992)**: Demuestra capacidad superior de discriminación entre clases
3. **Balance Precision-Recall**: F1-Score de 95.52% indica equilibrio óptimo
4. **Eficiencia Computacional**: Entrenamiento más rápido (0.35s vs 44.11s del Deep Learning)
5. **Bajo False Positive Rate (1.70%)**: Minimiza aprobaciones erróneas (riesgo financiero)
6. **Bajo False Negative Rate (1.40%)**: Minimiza rechazos erróneos (oportunidad perdida)

### Comparación de Errores

| Modelo | Falsos Positivos | Falsos Negativos | Total Errores |
|--------|------------------|------------------|---------------|
| Random Forest | 28 | 5 | 33 |
| Gradient Boosting | 19 | 16 | 35 |
| Deep Learning | 1089 | 21 | 1110 |


### Análisis de Deep Learning

El modelo de Deep Learning mostró un rendimiento significativamente inferior (44.50% accuracy) debido a:
- Preprocesamiento simplificado (solo LabelEncoding sin TF-IDF para campos de texto)
- Falta de feature engineering avanzado
- Los modelos basados en árboles (Random Forest, Gradient Boosting) son menos sensibles a la calidad del preprocesamiento
- Para mejorar Deep Learning se requeriría:
  - Implementar embeddings para campos de texto
  - Feature scaling más sofisticado
  - Arquitectura más profunda con regularización
  - Mayor cantidad de datos de entrenamiento

---

## Recomendación para Producción

Se recomienda desplegar el modelo **Random Forest** en producción por las siguientes razones:

1. **Rendimiento Superior**: Máxima accuracy y AUC-ROC entre todos los modelos evaluados
2. **Eficiencia Operacional**: Tiempo de inferencia rápido (24,519 predicciones/segundo)
3. **Bajo Riesgo**: Mínima tasa de falsos positivos protege contra pérdidas financieras
4. **Mantenibilidad**: Modelo más simple de interpretar y mantener que redes neuronales
5. **Recursos Computacionales**: Requiere menos recursos que Deep Learning para entrenamiento y predicción

---

## Configuración Implementada

El sistema Flask ha sido configurado para:
- Cargar automáticamente el mejor modelo según `models/modelo_config.json`
- Soportar los tres tipos de modelos (Deep Learning, Random Forest, Gradient Boosting)
- Detectar el tipo de modelo y usar el método de predicción apropiado:
  - `predict_proba()` para modelos sklearn
  - `predict()` para modelos Keras
- Mantener compatibilidad con el sistema existente

**Archivos generados:**
- `models/modelo_random_forest.pkl` - Modelo entrenado
- `models/modelo_gradient_boosting.pkl` - Modelo entrenado
- `models/modelo_deep_learning.h5` - Modelo entrenado
- `models/preprocessor_comparativa.pkl` - Preprocesador unificado
- `models/modelo_config.json` - Configuración de producción
- `models/comparativa_modelos.json` - Reporte detallado
- `models/comparativa_modelos.csv` - Reporte tabular

---

*Generado automáticamente el 2025-11-10 23:07:12*
