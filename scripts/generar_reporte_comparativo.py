"""
Script para visualizar la comparación de modelos
Genera un archivo markdown con tablas y gráficos de comparación
"""
import json
import pandas as pd
from datetime import datetime

# Cargar datos de comparación
with open('models/comparativa_modelos.json', 'r') as f:
    comparativa = json.load(f)

# Extraer información
mejor_modelo = comparativa['mejor_modelo']
fecha = comparativa['fecha_generacion']
modelos = comparativa['resumen_comparativo']

# Crear markdown
md_content = f"""# Comparación de Modelos de Machine Learning
## Sistema de Análisis de Créditos

**Fecha de generación:** {fecha}  
**Mejor modelo seleccionado:** {mejor_modelo}  
**Modelos comparados:** {len(modelos)}

---

## Resumen Ejecutivo

El análisis comparativo evaluó tres algoritmos de machine learning sobre el mismo conjunto de datos:
- **Deep Learning**: Red neuronal profunda de 5 capas
- **Random Forest**: Ensamble de 200 árboles de decisión  
- **Gradient Boosting**: 200 estimadores con boosting secuencial

### Métricas Principales

| Modelo | Accuracy | Precision | Recall | F1-Score | AUC-ROC | Log Loss |
|--------|----------|-----------|--------|----------|---------|----------|
"""

for modelo in modelos:
    md_content += f"| **{modelo['model_name']}** | "
    md_content += f"{modelo['accuracy']*100:.2f}% | "
    md_content += f"{modelo['precision']*100:.2f}% | "
    md_content += f"{modelo['recall']*100:.2f}% | "
    md_content += f"{modelo['f1_score']*100:.2f}% | "
    md_content += f"{modelo['auc_roc']:.4f} | "
    md_content += f"{modelo['log_loss']:.4f} |\n"

md_content += f"""

---

## Análisis Detallado por Modelo

"""

for modelo in modelos:
    cm = modelo['confusion_matrix']
    md_content += f"""
### {modelo['model_name']}

**Métricas de Clasificación:**
- **Accuracy:** {modelo['accuracy']*100:.2f}%
- **Precision:** {modelo['precision']*100:.2f}%
- **Recall:** {modelo['recall']*100:.2f}%
- **F1-Score:** {modelo['f1_score']*100:.2f}%
- **AUC-ROC:** {modelo['auc_roc']:.4f}
- **Log Loss:** {modelo['log_loss']:.4f}

**Métricas Adicionales:**
- **Specificity:** {modelo['specificity']*100:.2f}%
- **False Positive Rate:** {modelo['false_positive_rate']*100:.2f}%
- **False Negative Rate:** {modelo['false_negative_rate']*100:.2f}%

**Matriz de Confusión:**
```
                Predicho Negativo    Predicho Positivo
Real Negativo        {cm['true_negatives']:>5}              {cm['false_positives']:>5}
Real Positivo        {cm['false_negatives']:>5}              {cm['true_positives']:>5}
```

**Rendimiento Computacional:**
- **Tiempo de entrenamiento:** {modelo['training_time_seconds']:.2f} segundos
- **Tiempo de predicción:** {modelo['prediction_time_seconds']:.4f} segundos
- **Predicciones por segundo:** {modelo['predictions_per_second']:,.0f}

**Rankings:**
- Rank Accuracy: {modelo['rank_accuracy']:.1f}
- Rank AUC-ROC: {modelo['rank_auc_roc']:.1f}
- Rank F1-Score: {modelo['rank_f1_score']:.1f}
- **Rank Global: {modelo['rank_global']:.1f}**

---
"""

md_content += f"""
## Justificación de la Selección

El modelo **{mejor_modelo}** fue seleccionado como el mejor basándose en:

1. **Mayor Accuracy ({modelos[0]['accuracy']*100:.2f}%)**: Proporciona la mejor tasa de predicciones correctas
2. **Excelente AUC-ROC ({modelos[0]['auc_roc']:.4f})**: Demuestra capacidad superior de discriminación entre clases
3. **Balance Precision-Recall**: F1-Score de {modelos[0]['f1_score']*100:.2f}% indica equilibrio óptimo
4. **Eficiencia Computacional**: Entrenamiento más rápido ({modelos[0]['training_time_seconds']:.2f}s vs {modelos[2]['training_time_seconds']:.2f}s del Deep Learning)
5. **Bajo False Positive Rate ({modelos[0]['false_positive_rate']*100:.2f}%)**: Minimiza aprobaciones erróneas (riesgo financiero)
6. **Bajo False Negative Rate ({modelos[0]['false_negative_rate']*100:.2f}%)**: Minimiza rechazos erróneos (oportunidad perdida)

### Comparación de Errores

| Modelo | Falsos Positivos | Falsos Negativos | Total Errores |
|--------|------------------|------------------|---------------|
"""

for modelo in modelos:
    cm = modelo['confusion_matrix']
    total_errores = cm['false_positives'] + cm['false_negatives']
    md_content += f"| {modelo['model_name']} | {cm['false_positives']} | {cm['false_negatives']} | {total_errores} |\n"

md_content += f"""

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

Se recomienda desplegar el modelo **{mejor_modelo}** en producción por las siguientes razones:

1. **Rendimiento Superior**: Máxima accuracy y AUC-ROC entre todos los modelos evaluados
2. **Eficiencia Operacional**: Tiempo de inferencia rápido ({modelos[0]['predictions_per_second']:,.0f} predicciones/segundo)
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

*Generado automáticamente el {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""

# Guardar archivo markdown
with open('models/COMPARACION_MODELOS.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("✅ Documento de comparación generado: models/COMPARACION_MODELOS.md")
print(f"\n🏆 Mejor modelo: {mejor_modelo}")
print(f"📊 Accuracy: {modelos[0]['accuracy']*100:.2f}%")
print(f"📈 AUC-ROC: {modelos[0]['auc_roc']:.4f}")
