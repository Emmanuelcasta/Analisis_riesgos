"""
Script de prueba para verificar la carga del modelo
"""
import os
import json
import pickle
from tensorflow import keras

base_path = 'models'

# Verificar si existe configuración de modelo comparativo
config_path = os.path.join(base_path, 'modelo_config.json')
print(f"¿Existe config?: {os.path.exists(config_path)}")

if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print(f"Config: {json.dumps(config, indent=2)}")
    mejor_modelo = config.get('mejor_modelo', '')
    print(f"\n📊 Mejor modelo: {mejor_modelo}")
    
    # Cargar modelo según configuración
    if mejor_modelo == 'Random Forest':
        modelo_path = os.path.join(base_path, 'modelo_random_forest.pkl')
        print(f"Cargando desde: {modelo_path}")
        with open(modelo_path, 'rb') as f:
            modelo = pickle.load(f)
        print(f"✅ Modelo Random Forest cargado exitosamente")
        print(f"Tipo: {type(modelo)}")
        print(f"Tiene predict_proba?: {hasattr(modelo, 'predict_proba')}")
    
    # Cargar preprocessor comparativo
    preprocessor_path = os.path.join(base_path, 'preprocessor_comparativa.pkl')
    if os.path.exists(preprocessor_path):
        with open(preprocessor_path, 'rb') as f:
            preprocessor = pickle.load(f)
        print(f"✅ Preprocessor cargado")
    
    # Cargar métricas comparativas
    metricas_path = os.path.join(base_path, 'comparativa_modelos.json')
    if os.path.exists(metricas_path):
        with open(metricas_path, 'r') as f:
            comparativa = json.load(f)
        
        print(f"\n📈 Métricas del mejor modelo:")
        # Extraer métricas del mejor modelo
        for modelo_info in comparativa.get('resumen_comparativo', []):
            if modelo_info['model_name'] == mejor_modelo:
                metricas = {
                    'accuracy': modelo_info['accuracy'],
                    'precision': modelo_info['precision'],
                    'recall': modelo_info['recall'],
                    'f1_score': modelo_info['f1_score'],
                    'auc_roc': modelo_info['auc_roc'],
                    'samples_entrenamiento': 8000,
                    'fecha_entrenamiento': config.get('fecha_entrenamiento', 'N/A'),
                    'modelo': mejor_modelo
                }
                print(json.dumps(metricas, indent=2))
                break

print("\n✅ Test completado")
