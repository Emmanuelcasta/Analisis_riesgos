"""
Script principal para ejecutar la aplicación Flask
"""
from app import create_app
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np

# Clase PreprocessorNLP (necesaria para desserializar el pickle)
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

app = create_app()

if __name__ == '__main__':
    print("=" * 60)
    print("Sistema de Análisis de Préstamos con IA")
    print("=" * 60)
    print("\nIniciando servidor web...")
    print("Accede a: http://localhost:5000")
    print("\nPresiona Ctrl+C para detener el servidor\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
