"""
Script de Entrenamiento Comparativo de Modelos
===============================================
Entrena y compara 3 modelos de Machine Learning:
1. Deep Learning (Red Neuronal Profunda)
2. Random Forest Classifier
3. Gradient Boosting (XGBoost)

Genera reportes detallados de rendimiento para seleccionar el mejor modelo.
"""

import pandas as pd
import numpy as np
import json
import time
import pickle
import sys
import os
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, log_loss, confusion_matrix, classification_report
)
import warnings
warnings.filterwarnings('ignore')

# Importar TensorFlow/Keras
try:
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
    from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False
    print("⚠️  TensorFlow no disponible. Se entrenarán solo Random Forest y Gradient Boosting.")

# Preprocesador NLP (mismo del script original)
class PreprocessorNLP:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.text_vectorizers = {}
        self.feature_names = []
        
    def fit(self, X):
        # Guardar nombres de columnas
        self.feature_names = X.columns.tolist()
        
        # Identificar tipos de columnas
        numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
        
        # Guardar listas
        self.numeric_cols = numeric_cols
        self.categorical_cols = categorical_cols
        
        # Entrenar Label Encoders para categóricas
        for col in categorical_cols:
            le = LabelEncoder()
            le.fit(X[col].astype(str))
            self.label_encoders[col] = le
        
        # Entrenar Scaler en columnas numéricas
        if numeric_cols:
            self.scaler.fit(X[numeric_cols])
        
        return self
    
    def transform(self, X):
        X_transformed = X.copy()
        
        # Transformar categóricas (manejar valores no vistos)
        for col in self.categorical_cols:
            if col in X_transformed.columns:
                le = self.label_encoders[col]
                # Convertir a string
                valores = X_transformed[col].astype(str)
                # Reemplazar valores no vistos con el más común
                valores_conocidos = set(le.classes_)
                valores_unicos = valores.unique()
                valores_nuevos = [v for v in valores_unicos if v not in valores_conocidos]
                
                if valores_nuevos:
                    # Usar el valor más común (primera clase)
                    valor_default = le.classes_[0]
                    for v in valores_nuevos:
                        valores = valores.replace(v, valor_default)
                
                X_transformed[col] = le.transform(valores)
        
        # Escalar numéricas
        if self.numeric_cols:
            X_transformed[self.numeric_cols] = self.scaler.transform(X_transformed[self.numeric_cols])
        
        return X_transformed
    
    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)


def cargar_datos():
    """Carga el dataset de préstamos"""
    print("📂 Cargando datos...")
    
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    csv_path = os.path.join(data_dir, 'datos_prestamos.csv')
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset no encontrado: {csv_path}")
    
    df = pd.read_csv(csv_path)
    print(f"   ✓ Cargados {len(df)} registros")
    
    return df


def preparar_datos(df):
    """Prepara features y target"""
    print("\n🔧 Preparando datos...")
    
    # Columnas a excluir
    columnas_excluir = [
        'aprobado',  # Target
        'motivos_rechazo',  # Texto explicativo
        'documento_identidad',  # ID único
        'fecha_nacimiento',  # Fechas
        'fecha_expedicion_documento',
        'fecha_ingreso_empresa'
    ]
    
    # Features
    feature_cols = [col for col in df.columns if col not in columnas_excluir]
    X = df[feature_cols].copy()
    y = df['aprobado'].values
    
    print(f"   ✓ Features: {X.shape[1]} variables")
    print(f"   ✓ Target: {len(y)} muestras")
    print(f"   ✓ Balance: Aprobados={y.sum()} ({y.mean()*100:.1f}%), Rechazados={len(y)-y.sum()} ({(1-y.mean())*100:.1f}%)")
    
    return X, y, feature_cols


def entrenar_deep_learning(X_train, X_test, y_train, y_test):
    """Entrena modelo de Deep Learning (red neuronal profunda)"""
    print("\n" + "="*70)
    print("🧠 MODELO 1: DEEP LEARNING (Red Neuronal Profunda)")
    print("="*70)
    
    if not TF_AVAILABLE:
        print("❌ TensorFlow no disponible. Saltando modelo Deep Learning.")
        return None
    
    inicio = time.time()
    
    # Arquitectura
    input_dim = X_train.shape[1]
    
    model = Sequential([
        Dense(256, activation='relu', input_shape=(input_dim,)),
        BatchNormalization(),
        Dropout(0.3),
        
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.3),
        
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(0.2),
        
        Dense(32, activation='relu'),
        Dropout(0.2),
        
        Dense(1, activation='sigmoid')
    ])
    
    # Compilar
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy', tf.keras.metrics.AUC(name='auc'),
                 tf.keras.metrics.Precision(name='precision'),
                 tf.keras.metrics.Recall(name='recall')]
    )
    
    print(f"   ✓ Arquitectura: {model.count_params()} parámetros")
    
    # Callbacks
    early_stop = EarlyStopping(monitor='val_auc', patience=15, restore_best_weights=True, mode='max')
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-7)
    
    # Pesos de clase (para desbalance)
    class_weight = {
        0: len(y_train) / (2 * (len(y_train) - y_train.sum())),
        1: len(y_train) / (2 * y_train.sum())
    }
    
    # Entrenar
    print("   ⏳ Entrenando (max 100 épocas)...")
    history = model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=32,
        validation_split=0.2,
        callbacks=[early_stop, reduce_lr],
        class_weight=class_weight,
        verbose=0
    )
    
    tiempo_entrenamiento = time.time() - inicio
    
    # Predicciones
    inicio_pred = time.time()
    y_pred_proba = model.predict(X_test, verbose=0).flatten()
    y_pred = (y_pred_proba > 0.5).astype(int)
    tiempo_prediccion = time.time() - inicio_pred
    
    # Métricas
    metricas = calcular_metricas(y_test, y_pred, y_pred_proba, 
                                  tiempo_entrenamiento, tiempo_prediccion,
                                  "Deep Learning")
    
    print(f"   ✅ Entrenamiento completado en {tiempo_entrenamiento:.2f}s")
    print(f"   📊 Accuracy: {metricas['accuracy']*100:.2f}%")
    print(f"   📊 AUC-ROC: {metricas['auc_roc']:.4f}")
    
    return {
        'model': model,
        'metrics': metricas,
        'history': history.history
    }


def entrenar_random_forest(X_train, X_test, y_train, y_test):
    """Entrena modelo de Random Forest"""
    print("\n" + "="*70)
    print("🌲 MODELO 2: RANDOM FOREST")
    print("="*70)
    
    inicio = time.time()
    
    # Configuración
    rf_model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=5,
        max_features='sqrt',
        class_weight='balanced',
        random_state=42,
        n_jobs=-1,
        verbose=0
    )
    
    print(f"   ✓ Configuración: {rf_model.n_estimators} árboles, max_depth={rf_model.max_depth}")
    
    # Entrenar
    print("   ⏳ Entrenando...")
    rf_model.fit(X_train, y_train)
    
    tiempo_entrenamiento = time.time() - inicio
    
    # Predicciones
    inicio_pred = time.time()
    y_pred_proba = rf_model.predict_proba(X_test)[:, 1]
    y_pred = rf_model.predict(X_test)
    tiempo_prediccion = time.time() - inicio_pred
    
    # Métricas
    metricas = calcular_metricas(y_test, y_pred, y_pred_proba,
                                  tiempo_entrenamiento, tiempo_prediccion,
                                  "Random Forest")
    
    # Feature importance
    feature_importance = rf_model.feature_importances_
    
    print(f"   ✅ Entrenamiento completado en {tiempo_entrenamiento:.2f}s")
    print(f"   📊 Accuracy: {metricas['accuracy']*100:.2f}%")
    print(f"   📊 AUC-ROC: {metricas['auc_roc']:.4f}")
    
    return {
        'model': rf_model,
        'metrics': metricas,
        'feature_importance': feature_importance
    }


def entrenar_gradient_boosting(X_train, X_test, y_train, y_test):
    """Entrena modelo de Gradient Boosting"""
    print("\n" + "="*70)
    print("⚡ MODELO 3: GRADIENT BOOSTING")
    print("="*70)
    
    inicio = time.time()
    
    # Configuración
    gb_model = GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        min_samples_split=10,
        min_samples_leaf=5,
        subsample=0.8,
        random_state=42,
        verbose=0
    )
    
    print(f"   ✓ Configuración: {gb_model.n_estimators} estimadores, lr={gb_model.learning_rate}")
    
    # Entrenar
    print("   ⏳ Entrenando...")
    gb_model.fit(X_train, y_train)
    
    tiempo_entrenamiento = time.time() - inicio
    
    # Predicciones
    inicio_pred = time.time()
    y_pred_proba = gb_model.predict_proba(X_test)[:, 1]
    y_pred = gb_model.predict(X_test)
    tiempo_prediccion = time.time() - inicio_pred
    
    # Métricas
    metricas = calcular_metricas(y_test, y_pred, y_pred_proba,
                                  tiempo_entrenamiento, tiempo_prediccion,
                                  "Gradient Boosting")
    
    # Feature importance
    feature_importance = gb_model.feature_importances_
    
    print(f"   ✅ Entrenamiento completado en {tiempo_entrenamiento:.2f}s")
    print(f"   📊 Accuracy: {metricas['accuracy']*100:.2f}%")
    print(f"   📊 AUC-ROC: {metricas['auc_roc']:.4f}")
    
    return {
        'model': gb_model,
        'metrics': metricas,
        'feature_importance': feature_importance
    }


def calcular_metricas(y_true, y_pred, y_pred_proba, tiempo_entrenamiento, tiempo_prediccion, nombre_modelo):
    """Calcula métricas completas de evaluación"""
    
    # Métricas básicas
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)
    auc_roc = roc_auc_score(y_true, y_pred_proba)
    
    # Log Loss
    try:
        logloss = log_loss(y_true, y_pred_proba)
    except:
        logloss = None
    
    # Matriz de confusión
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    
    # Especificidad
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    
    # False Positive Rate
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    
    # False Negative Rate
    fnr = fn / (fn + tp) if (fn + tp) > 0 else 0
    
    return {
        'model_name': nombre_modelo,
        'accuracy': float(accuracy),
        'precision': float(precision),
        'recall': float(recall),
        'f1_score': float(f1),
        'auc_roc': float(auc_roc),
        'log_loss': float(logloss) if logloss is not None else None,
        'specificity': float(specificity),
        'false_positive_rate': float(fpr),
        'false_negative_rate': float(fnr),
        'confusion_matrix': {
            'true_negatives': int(tn),
            'false_positives': int(fp),
            'false_negatives': int(fn),
            'true_positives': int(tp)
        },
        'training_time_seconds': float(tiempo_entrenamiento),
        'prediction_time_seconds': float(tiempo_prediccion),
        'predictions_per_second': float(len(y_true) / tiempo_prediccion) if tiempo_prediccion > 0 else 0
    }


def generar_reportes(resultados, output_dir):
    """Genera reportes comparativos en JSON y CSV"""
    print("\n" + "="*70)
    print("📊 GENERANDO REPORTES COMPARATIVOS")
    print("="*70)
    
    # Filtrar modelos entrenados
    modelos_entrenados = {k: v for k, v in resultados.items() if v is not None}
    
    if not modelos_entrenados:
        print("❌ No hay modelos entrenados para comparar")
        return
    
    # Crear DataFrame comparativo
    metricas_df = pd.DataFrame([v['metrics'] for v in modelos_entrenados.values()])
    
    # Ranking (mejor a peor)
    metricas_df['rank_accuracy'] = metricas_df['accuracy'].rank(ascending=False)
    metricas_df['rank_auc_roc'] = metricas_df['auc_roc'].rank(ascending=False)
    metricas_df['rank_f1_score'] = metricas_df['f1_score'].rank(ascending=False)
    
    # Score global (promedio de rankings)
    metricas_df['rank_global'] = (
        metricas_df['rank_accuracy'] + 
        metricas_df['rank_auc_roc'] + 
        metricas_df['rank_f1_score']
    ) / 3
    
    # Ordenar por ranking global
    metricas_df = metricas_df.sort_values('rank_global')
    
    # Mejor modelo
    mejor_modelo = metricas_df.iloc[0]['model_name']
    
    print(f"\n🏆 MEJOR MODELO: {mejor_modelo}")
    print(f"   📊 Accuracy: {metricas_df.iloc[0]['accuracy']*100:.2f}%")
    print(f"   📊 AUC-ROC: {metricas_df.iloc[0]['auc_roc']:.4f}")
    print(f"   📊 F1-Score: {metricas_df.iloc[0]['f1_score']:.4f}")
    print(f"   ⏱️  Tiempo entrenamiento: {metricas_df.iloc[0]['training_time_seconds']:.2f}s")
    print(f"   ⚡ Predicciones/segundo: {metricas_df.iloc[0]['predictions_per_second']:.0f}")
    
    # Guardar CSV
    csv_path = os.path.join(output_dir, 'comparativa_modelos.csv')
    metricas_df.to_csv(csv_path, index=False)
    print(f"\n✓ Reporte CSV guardado: {csv_path}")
    
    # Preparar JSON
    reporte_json = {
        'fecha_generacion': datetime.now().isoformat(),
        'mejor_modelo': mejor_modelo,
        'modelos_comparados': len(modelos_entrenados),
        'resumen_comparativo': metricas_df.to_dict('records'),
        'detalles_mejor_modelo': metricas_df.iloc[0].to_dict(),
        'recomendacion': f"Se recomienda usar {mejor_modelo} para producción debido a su mejor balance entre precisión ({metricas_df.iloc[0]['accuracy']*100:.2f}%), AUC-ROC ({metricas_df.iloc[0]['auc_roc']:.4f}) y tiempo de predicción ({metricas_df.iloc[0]['prediction_time_seconds']:.4f}s)."
    }
    
    # Guardar JSON
    json_path = os.path.join(output_dir, 'comparativa_modelos.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(reporte_json, f, indent=2, ensure_ascii=False)
    print(f"✓ Reporte JSON guardado: {json_path}")
    
    # Tabla comparativa en consola
    print("\n" + "="*70)
    print("📋 TABLA COMPARATIVA DE MODELOS")
    print("="*70)
    print(f"\n{'Modelo':<20} {'Accuracy':<10} {'AUC-ROC':<10} {'F1-Score':<10} {'Train(s)':<10} {'Pred/s':<10}")
    print("-"*70)
    for _, row in metricas_df.iterrows():
        print(f"{row['model_name']:<20} {row['accuracy']*100:>8.2f}% {row['auc_roc']:>9.4f} {row['f1_score']:>9.4f} {row['training_time_seconds']:>9.2f} {row['predictions_per_second']:>9.0f}")
    
    return mejor_modelo


def guardar_modelos(resultados, preprocessor, output_dir):
    """Guarda todos los modelos entrenados"""
    print("\n💾 Guardando modelos...")
    
    modelos_guardados = []
    
    for nombre, resultado in resultados.items():
        if resultado is None:
            continue
        
        model = resultado['model']
        nombre_archivo = nombre.lower().replace(' ', '_')
        
        if nombre == 'deep_learning':
            # Guardar modelo Keras
            model_path = os.path.join(output_dir, f'modelo_{nombre_archivo}.h5')
            model.save(model_path)
            print(f"   ✓ {nombre}: {model_path}")
        else:
            # Guardar modelo sklearn con pickle
            model_path = os.path.join(output_dir, f'modelo_{nombre_archivo}.pkl')
            with open(model_path, 'wb') as f:
                pickle.dump(model, f)
            print(f"   ✓ {nombre}: {model_path}")
        
        modelos_guardados.append(nombre)
    
    # Guardar preprocessor
    preprocessor_path = os.path.join(output_dir, 'preprocessor_comparativa.pkl')
    with open(preprocessor_path, 'wb') as f:
        pickle.dump(preprocessor, f)
    print(f"   ✓ Preprocessor: {preprocessor_path}")
    
    return modelos_guardados


def main():
    print("="*70)
    print("🚀 ENTRENAMIENTO COMPARATIVO DE MODELOS")
    print("="*70)
    print("Modelos a entrenar:")
    print("  1. Deep Learning (Red Neuronal Profunda)")
    print("  2. Random Forest Classifier")
    print("  3. Gradient Boosting Classifier")
    print("="*70)
    
    try:
        # 1. Cargar datos
        df = cargar_datos()
        
        # 2. Preparar datos
        X, y, feature_cols = preparar_datos(df)
        
        # 3. Dividir train-test
        print("\n📊 Dividiendo datos (80-20 estratificado)...")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        print(f"   ✓ Train: {len(X_train)} muestras")
        print(f"   ✓ Test: {len(X_test)} muestras")
        
        # 4. Preprocesar
        print("\n🔧 Preprocesando datos...")
        preprocessor = PreprocessorNLP()
        X_train_processed = preprocessor.fit_transform(X_train)
        X_test_processed = preprocessor.transform(X_test)
        
        # Asegurar que todo es numérico
        X_train_processed = X_train_processed.apply(pd.to_numeric, errors='coerce').fillna(0)
        X_test_processed = X_test_processed.apply(pd.to_numeric, errors='coerce').fillna(0)
        
        # Convertir a numpy arrays
        X_train_np = X_train_processed.values.astype(np.float32)
        X_test_np = X_test_processed.values.astype(np.float32)
        
        print(f"   ✓ Dimensión final: {X_train_np.shape[1]} features")
        print(f"   ✓ Tipos de datos verificados: {X_train_np.dtype}")
        
        # 5. Entrenar modelos
        resultados = {}
        
        # Deep Learning
        resultados['deep_learning'] = entrenar_deep_learning(
            X_train_np, X_test_np, y_train, y_test
        )
        
        # Random Forest
        resultados['random_forest'] = entrenar_random_forest(
            X_train_np, X_test_np, y_train, y_test
        )
        
        # Gradient Boosting
        resultados['gradient_boosting'] = entrenar_gradient_boosting(
            X_train_np, X_test_np, y_train, y_test
        )
        
        # 6. Generar reportes
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
        os.makedirs(output_dir, exist_ok=True)
        
        mejor_modelo = generar_reportes(resultados, output_dir)
        
        # 7. Guardar modelos
        guardar_modelos(resultados, preprocessor, output_dir)
        
        # 8. Crear archivo de configuración
        config = {
            'mejor_modelo': mejor_modelo,
            'fecha_entrenamiento': datetime.now().isoformat(),
            'modelos_disponibles': list(resultados.keys())
        }
        
        config_path = os.path.join(output_dir, 'modelo_config.json')
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print("\n" + "="*70)
        print("✅ PROCESO COMPLETADO EXITOSAMENTE")
        print("="*70)
        print(f"\n📁 Archivos generados en: {output_dir}")
        print("   • comparativa_modelos.json - Reporte detallado JSON")
        print("   • comparativa_modelos.csv - Tabla comparativa CSV")
        print("   • modelo_deep_learning.h5 - Modelo Deep Learning")
        print("   • modelo_random_forest.pkl - Modelo Random Forest")
        print("   • modelo_gradient_boosting.pkl - Modelo Gradient Boosting")
        print("   • preprocessor_comparativa.pkl - Preprocesador de datos")
        print("   • modelo_config.json - Configuración del mejor modelo")
        
        print(f"\n🏆 MODELO RECOMENDADO PARA PRODUCCIÓN: {mejor_modelo}")
        
    except Exception as e:
        print(f"\n❌ ERROR durante el entrenamiento:")
        print(f"   {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
