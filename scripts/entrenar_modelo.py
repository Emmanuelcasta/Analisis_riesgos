"""
Entrenamiento de red neuronal profunda con procesamiento NLP para análisis de préstamos
"""
import pandas as pd
import numpy as np
import pickle
import json
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

import matplotlib.pyplot as plt

# Configurar semilla para reproducibilidad
np.random.seed(42)
tf.random.set_seed(42)

class PreprocessorNLP:
    """Preprocesador con capacidades de NLP para campos de texto"""
    
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.text_vectorizers = {}
        self.categorical_features = []
        self.numerical_features = []
        self.text_features = []
        
    def fit(self, df):
        """Ajusta los preprocesadores al dataset"""
        
        # Definir tipos de features
        self.text_features = [
            'ocupacion', 'sector_economico', 'actividad_economica_independiente',
            'titulo_profesional', 'fuente_ingresos_principal', 'cargo_empleado'
        ]
        
        self.categorical_features = [
            'tipo_documento', 'estado_civil', 'genero', 'tipo_contrato',
            'nivel_estudios', 'linea_credito', 'departamento_residencia',
            'ciudad_residencia'
        ]
        
        self.numerical_features = [
            'edad', 'personas_a_cargo', 'años_domicilio', 'tiempo_desarrollo_actividad',
            'tiempo_en_actividad', 'ingreso_principal', 'otros_ingresos',
            'gastos_mensuales', 'monto_solicitado', 'plazo_meses',
            'capacidad_pago', 'ratio_endeudamiento'
        ]
        
        # Boolean features
        self.boolean_features = ['es_arrendador']
        
        # Entrenar Label Encoders para categóricas
        for col in self.categorical_features:
            le = LabelEncoder()
            # Manejar valores nulos
            df[col] = df[col].fillna('desconocido')
            le.fit(df[col].astype(str))
            self.label_encoders[col] = le
        
        # Entrenar vectorizadores de texto (Tokenización simple con TF-IDF simulado)
        for col in self.text_features:
            # Crear vocabulario único
            df[col] = df[col].fillna('')
            unique_values = df[col].astype(str).unique()
            vocab = {val: idx for idx, val in enumerate(unique_values)}
            self.text_vectorizers[col] = vocab
        
        # Ajustar scaler para features numéricas
        numerical_data = df[self.numerical_features].fillna(0)
        self.scaler.fit(numerical_data)
        
        return self
    
    def transform(self, df):
        """Transforma el dataset usando los preprocesadores ajustados"""
        features = []
        
        # 1. Features numéricas normalizadas
        numerical_data = df[self.numerical_features].fillna(0)
        numerical_scaled = self.scaler.transform(numerical_data)
        features.append(numerical_scaled)
        
        # 2. Features categóricas codificadas
        for col in self.categorical_features:
            df[col] = df[col].fillna('desconocido')
            encoded = self.label_encoders[col].transform(df[col].astype(str))
            features.append(encoded.reshape(-1, 1))
        
        # 3. Features de texto vectorizadas (embeddings simplificados)
        for col in self.text_features:
            df[col] = df[col].fillna('')
            vocab = self.text_vectorizers[col]
            # Convertir a índices
            encoded = df[col].astype(str).apply(
                lambda x: vocab.get(x, 0)
            ).values
            features.append(encoded.reshape(-1, 1))
        
        # 4. Features booleanas
        for col in self.boolean_features:
            boolean_data = df[col].astype(int).values
            features.append(boolean_data.reshape(-1, 1))
        
        # Concatenar todas las features
        X = np.concatenate(features, axis=1)
        return X
    
    def fit_transform(self, df):
        """Ajusta y transforma en un solo paso"""
        self.fit(df)
        return self.transform(df)

def crear_modelo_deep_learning(input_dim):
    """
    Crea una red neuronal profunda para clasificación de préstamos
    Arquitectura optimizada para análisis de riesgo crediticio
    """
    model = keras.Sequential([
        # Capa de entrada
        layers.Input(shape=(input_dim,)),
        
        # Primera capa densa con regularización
        layers.Dense(256, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        layers.BatchNormalization(),
        layers.Dropout(0.4),
        
        # Segunda capa densa
        layers.Dense(128, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        
        # Tercera capa densa
        layers.Dense(64, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        layers.BatchNormalization(),
        layers.Dropout(0.3),
        
        # Cuarta capa densa
        layers.Dense(32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)),
        layers.Dropout(0.2),
        
        # Capa de salida (clasificación binaria)
        layers.Dense(1, activation='sigmoid')
    ])
    
    # Compilar modelo con optimizador Adam
    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.001),
        loss='binary_crossentropy',
        metrics=[
            'accuracy',
            keras.metrics.Precision(name='precision'),
            keras.metrics.Recall(name='recall'),
            keras.metrics.AUC(name='auc')
        ]
    )
    
    return model

def entrenar_modelo():
    """Función principal de entrenamiento"""
    
    print("="*70)
    print("🚀 SISTEMA DE ANÁLISIS DE PRÉSTAMOS CON DEEP LEARNING Y NLP")
    print("="*70)
    
    # 1. Cargar datos
    print("\n📂 Cargando datos...")
    import os
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'datos_prestamos.csv')
    df = pd.read_csv(data_path)
    print(f"   ✓ Cargados {len(df)} registros")
    print(f"   ✓ Aprobados: {df['aprobado'].sum()} | Rechazados: {(1-df['aprobado']).sum()}")
    
    # 2. Separar features y target
    print("\n🔧 Preparando datos con procesamiento NLP...")
    y = df['aprobado'].values
    
    # Inicializar preprocesador con NLP
    preprocessor = PreprocessorNLP()
    X = preprocessor.fit_transform(df)
    
    print(f"   ✓ Dimensión de features: {X.shape}")
    print(f"   ✓ Features numéricas: {len(preprocessor.numerical_features)}")
    print(f"   ✓ Features categóricas: {len(preprocessor.categorical_features)}")
    print(f"   ✓ Features de texto (NLP): {len(preprocessor.text_features)}")
    
    # 3. Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"\n📊 División de datos:")
    print(f"   ✓ Entrenamiento: {len(X_train)} muestras")
    print(f"   ✓ Prueba: {len(X_test)} muestras")
    
    # 4. Crear modelo
    print("\n🧠 Creando red neuronal profunda...")
    model = crear_modelo_deep_learning(X_train.shape[1])
    print(model.summary())
    
    # Crear carpeta models si no existe
    models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    os.makedirs(models_dir, exist_ok=True)
    
    # 5. Configurar callbacks
    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=15,
        restore_best_weights=True,
        verbose=1
    )
    
    checkpoint_path = os.path.join(models_dir, 'modelo_prestamos_best.h5')
    checkpoint = ModelCheckpoint(
        checkpoint_path,
        monitor='val_auc',
        save_best_only=True,
        mode='max',
        verbose=1
    )
    
    # 6. Entrenar modelo
    print("\n🔥 Iniciando entrenamiento...")
    print("   (Esto puede tomar algunos minutos...)")
    
    history = model.fit(
        X_train, y_train,
        epochs=100,
        batch_size=32,
        validation_split=0.2,
        callbacks=[early_stopping, checkpoint],
        verbose=1
    )
    
    # 7. Evaluar modelo
    print("\n📈 Evaluando modelo en conjunto de prueba...")
    test_loss, test_acc, test_precision, test_recall, test_auc = model.evaluate(
        X_test, y_test, verbose=0
    )
    
    print(f"\n{'='*70}")
    print("📊 MÉTRICAS DEL MODELO")
    print(f"{'='*70}")
    print(f"   Accuracy:  {test_acc:.4f} ({test_acc*100:.2f}%)")
    print(f"   Precision: {test_precision:.4f}")
    print(f"   Recall:    {test_recall:.4f}")
    print(f"   AUC-ROC:   {test_auc:.4f}")
    print(f"   Loss:      {test_loss:.4f}")
    
    # Predicciones
    y_pred_proba = model.predict(X_test, verbose=0)
    y_pred = (y_pred_proba > 0.5).astype(int).flatten()
    
    # Reporte de clasificación
    print(f"\n{'='*70}")
    print("📋 REPORTE DETALLADO DE CLASIFICACIÓN")
    print(f"{'='*70}")
    print(classification_report(y_test, y_pred, target_names=['Rechazado', 'Aprobado']))
    
    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n🔍 Matriz de Confusión:")
    print(f"   [[TN={cm[0,0]:4d}  FP={cm[0,1]:4d}]")
    print(f"    [FN={cm[1,0]:4d}  TP={cm[1,1]:4d}]]")
    
    # 8. Guardar modelo y preprocesador
    print(f"\n💾 Guardando modelo y preprocesadores...")
    
    # Guardar modelo de Keras
    model_path = os.path.join(models_dir, 'modelo_prestamos_final.h5')
    model.save(model_path)
    print(f"   ✓ Modelo guardado: {model_path}")
    
    # Guardar preprocesador
    preprocessor_path = os.path.join(models_dir, 'preprocessor.pkl')
    with open(preprocessor_path, 'wb') as f:
        pickle.dump(preprocessor, f)
    print("   ✓ Preprocesador guardado: preprocessor.pkl")
    
    # Guardar historial de entrenamiento
    historial = {
        'loss': [float(x) for x in history.history['loss']],
        'accuracy': [float(x) for x in history.history['accuracy']],
        'val_loss': [float(x) for x in history.history['val_loss']],
        'val_accuracy': [float(x) for x in history.history['val_accuracy']],
        'auc': [float(x) for x in history.history['auc']],
        'val_auc': [float(x) for x in history.history['val_auc']]
    }
    
    with open('historial_entrenamiento.json', 'w') as f:
        json.dump(historial, f, indent=2)
    print("   ✓ Historial guardado: historial_entrenamiento.json")
    
    # Guardar métricas finales
    metricas = {
        'fecha_entrenamiento': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'num_muestras_entrenamiento': int(len(X_train)),
        'num_muestras_prueba': int(len(X_test)),
        'accuracy': float(test_acc),
        'precision': float(test_precision),
        'recall': float(test_recall),
        'auc_roc': float(test_auc),
        'loss': float(test_loss),
        'matriz_confusion': {
            'true_negative': int(cm[0,0]),
            'false_positive': int(cm[0,1]),
            'false_negative': int(cm[1,0]),
            'true_positive': int(cm[1,1])
        }
    }
    
    metricas_path = os.path.join(models_dir, 'metricas_modelo.json')
    with open(metricas_path, 'w') as f:
        json.dump(metricas, f, indent=2)
    print(f"   ✓ Métricas guardadas: {metricas_path}")
    
    # 9. Visualizar curvas de aprendizaje
    print("\n📊 Generando gráficas de rendimiento...")
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Accuracy
    axes[0, 0].plot(history.history['accuracy'], label='Train')
    axes[0, 0].plot(history.history['val_accuracy'], label='Validation')
    axes[0, 0].set_title('Accuracy durante entrenamiento')
    axes[0, 0].set_xlabel('Época')
    axes[0, 0].set_ylabel('Accuracy')
    axes[0, 0].legend()
    axes[0, 0].grid(True)
    
    # Loss
    axes[0, 1].plot(history.history['loss'], label='Train')
    axes[0, 1].plot(history.history['val_loss'], label='Validation')
    axes[0, 1].set_title('Loss durante entrenamiento')
    axes[0, 1].set_xlabel('Época')
    axes[0, 1].set_ylabel('Loss')
    axes[0, 1].legend()
    axes[0, 1].grid(True)
    
    # AUC
    axes[1, 0].plot(history.history['auc'], label='Train')
    axes[1, 0].plot(history.history['val_auc'], label='Validation')
    axes[1, 0].set_title('AUC-ROC durante entrenamiento')
    axes[1, 0].set_xlabel('Época')
    axes[1, 0].set_ylabel('AUC')
    axes[1, 0].legend()
    axes[1, 0].grid(True)
    
    # Curva ROC
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    axes[1, 1].plot(fpr, tpr, label=f'ROC (AUC = {test_auc:.3f})')
    axes[1, 1].plot([0, 1], [0, 1], 'k--', label='Random')
    axes[1, 1].set_title('Curva ROC')
    axes[1, 1].set_xlabel('Tasa Falsos Positivos')
    axes[1, 1].set_ylabel('Tasa Verdaderos Positivos')
    axes[1, 1].legend()
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.savefig('rendimiento_modelo.png', dpi=300, bbox_inches='tight')
    print("   ✓ Gráficas guardadas: rendimiento_modelo.png")
    
    print(f"\n{'='*70}")
    print("✅ ENTRENAMIENTO COMPLETADO EXITOSAMENTE")
    print(f"{'='*70}")
    print("\n📁 Archivos generados:")
    print("   • modelo_prestamos_final.h5 - Modelo de red neuronal")
    print("   • modelo_prestamos_best.h5 - Mejor modelo durante entrenamiento")
    print("   • preprocessor.pkl - Preprocesador con NLP")
    print("   • historial_entrenamiento.json - Historial completo")
    print("   • metricas_modelo.json - Métricas finales")
    print("   • rendimiento_modelo.png - Gráficas de rendimiento")
    print(f"\n{'='*70}\n")
    
    return model, preprocessor, metricas

if __name__ == '__main__':
    modelo, preprocessor, metricas = entrenar_modelo()
