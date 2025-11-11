"""
Rutas principales de la aplicación Flask
"""
from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import numpy as np
from datetime import datetime
import pickle
import json
import os
from tensorflow import keras
from sklearn.preprocessing import StandardScaler, LabelEncoder

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

main = Blueprint('main', __name__)

# Variables globales para el modelo (se cargan una vez)
modelo = None
preprocessor = None
metricas = None

def cargar_modelo():
    """Carga el modelo entrenado y el preprocesador"""
    global modelo, preprocessor, metricas
    
    if modelo is None:
        try:
            base_path = os.path.join(os.path.dirname(__file__), '..', 'models')
            
            # Verificar si existe configuración de modelo comparativo
            config_path = os.path.join(base_path, 'modelo_config.json')
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    config = json.load(f)
                
                mejor_modelo = config.get('mejor_modelo', '')
                print(f"📊 Cargando modelo: {mejor_modelo}")
                
                # Cargar modelo según configuración
                if mejor_modelo == 'Random Forest':
                    modelo_path = os.path.join(base_path, 'modelo_random_forest.pkl')
                    with open(modelo_path, 'rb') as f:
                        modelo = pickle.load(f)
                    print(f"✅ Modelo Random Forest cargado (Accuracy: {config.get('accuracy', 'N/A')}%)")
                elif mejor_modelo == 'Gradient Boosting':
                    modelo_path = os.path.join(base_path, 'modelo_gradient_boosting.pkl')
                    with open(modelo_path, 'rb') as f:
                        modelo = pickle.load(f)
                    print(f"✅ Modelo Gradient Boosting cargado (Accuracy: {config.get('accuracy', 'N/A')}%)")
                elif mejor_modelo == 'Deep Learning':
                    modelo_path = os.path.join(base_path, 'modelo_deep_learning.h5')
                    modelo = keras.models.load_model(modelo_path)
                    print(f"✅ Modelo Deep Learning cargado (Accuracy: {config.get('accuracy', 'N/A')}%)")
                
                # Cargar preprocessor comparativo
                preprocessor_path = os.path.join(base_path, 'preprocessor_comparativa.pkl')
                if os.path.exists(preprocessor_path):
                    with open(preprocessor_path, 'rb') as f:
                        preprocessor = pickle.load(f)
                
                # Cargar métricas comparativas y extraer las del mejor modelo
                metricas_path = os.path.join(base_path, 'comparativa_modelos.json')
                if os.path.exists(metricas_path):
                    with open(metricas_path, 'r') as f:
                        comparativa = json.load(f)
                    
                    # Extraer métricas del mejor modelo
                    for modelo_info in comparativa.get('resumen_comparativo', []):
                        if modelo_info['model_name'] == mejor_modelo:
                            metricas = {
                                'accuracy': modelo_info['accuracy'],
                                'precision': modelo_info['precision'],
                                'recall': modelo_info['recall'],
                                'f1_score': modelo_info['f1_score'],
                                'auc_roc': modelo_info['auc_roc'],
                                'samples_entrenamiento': 8000,  # From train/test split
                                'fecha_entrenamiento': config.get('fecha_entrenamiento', 'N/A'),
                                'modelo': mejor_modelo
                            }
                            break
                else:
                    metricas = {
                        'accuracy': 0.0,
                        'precision': 0.0,
                        'recall': 0.0,
                        'f1_score': 0.0,
                        'auc_roc': 0.0,
                        'samples_entrenamiento': 0,
                        'fecha_entrenamiento': 'N/A',
                        'modelo': 'Unknown'
                    }
            else:
                # Fallback al modelo original si no existe comparativa
                modelo_path = os.path.join(base_path, 'modelo_prestamos_final.h5')
                preprocessor_path = os.path.join(base_path, 'preprocessor.pkl')
                metricas_path = os.path.join(base_path, 'metricas_modelo.json')
                
                modelo = keras.models.load_model(modelo_path)
                with open(preprocessor_path, 'rb') as f:
                    preprocessor = pickle.load(f)
                with open(metricas_path, 'r') as f:
                    metricas = json.load(f)
                print("✅ Modelo original Deep Learning cargado (fallback)")
            
            return True
        except Exception as e:
            print(f"❌ Error al cargar el modelo: {e}")
            return False
    return True

def calcular_variables_derivadas(datos):
    """Calcula variables financieras derivadas"""
    capacidad_pago = datos['ingreso_principal'] + datos['otros_ingresos'] - datos['gastos_mensuales']
    cuota_estimada = datos['monto_solicitado'] * 0.025  # Estimación simplificada
    
    total_ingresos = datos['ingreso_principal'] + datos['otros_ingresos']
    ratio_endeudamiento = cuota_estimada / total_ingresos if total_ingresos > 0 else 1
    
    return capacidad_pago, cuota_estimada, ratio_endeudamiento

@main.route('/')
def index():
    """Página principal con el formulario"""
    # Cargar el modelo al inicio
    if not cargar_modelo():
        return render_template('error.html', 
                             mensaje="No se pudo cargar el modelo. Por favor entrene el modelo primero.")
    
    return render_template('index.html', metricas=metricas)

@main.route('/analizar', methods=['POST'])
def analizar():
    """Procesa el formulario y realiza la predicción"""
    if not cargar_modelo():
        return jsonify({'error': 'Modelo no disponible'}), 500
    
    try:
        # Obtener datos del formulario
        form_data = request.form
        
        # Calcular edad desde fecha de nacimiento
        fecha_nacimiento_str = form_data.get('fecha_nacimiento')
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d')
        edad = datetime.now().year - fecha_nacimiento.year
        
        # Convertir valores numéricos
        ingreso_principal = float(form_data.get('ingreso_principal', 0))
        otros_ingresos = float(form_data.get('otros_ingresos', 0))
        gastos_mensuales = float(form_data.get('gastos_mensuales', 0))
        monto_solicitado = float(form_data.get('monto_solicitado', 0))
        
        # Preparar datos de entrada
        datos_entrada = {
            'tipo_documento': form_data.get('tipo_documento'),
            'documento_identidad': int(form_data.get('documento_identidad', 0)),
            'primer_nombre': form_data.get('primer_nombre'),
            'segundo_nombre': form_data.get('segundo_nombre', ''),
            'primer_apellido': form_data.get('primer_apellido'),
            'segundo_apellido': form_data.get('segundo_apellido', ''),
            'celular': form_data.get('celular'),
            'correo_electronico': form_data.get('correo_electronico'),
            'pais_residencia': 'Colombia',
            'departamento_residencia': form_data.get('departamento_residencia'),
            'ciudad_residencia': form_data.get('ciudad_residencia'),
            'direccion_residencia': form_data.get('direccion_residencia'),
            'es_arrendador': form_data.get('es_arrendador') == 'on',
            'años_domicilio': int(form_data.get('años_domicilio', 0)),
            'fecha_nacimiento': fecha_nacimiento,
            'pais_nacimiento': 'Colombia',
            'departamento_nacimiento': form_data.get('departamento_residencia'),
            'ciudad_nacimiento': form_data.get('ciudad_residencia'),
            'fecha_expedicion_documento': fecha_nacimiento,
            'pais_expedicion': 'Colombia',
            'departamento_expedicion': form_data.get('departamento_residencia'),
            'ciudad_expedicion': form_data.get('ciudad_residencia'),
            'linea_credito': form_data.get('linea_credito'),
            'plazo_meses': int(form_data.get('plazo_meses', 12)),
            'edad': edad,
            'estado_civil': form_data.get('estado_civil'),
            'personas_a_cargo': int(form_data.get('personas_a_cargo', 0)),
            'genero': form_data.get('genero'),
            'ocupacion': form_data.get('ocupacion'),
            'cargo_empleado': form_data.get('cargo_empleado', ''),
            'tipo_contrato': form_data.get('tipo_contrato'),
            'fecha_ingreso_empresa': datetime.now(),
            'actividad_economica_independiente': form_data.get('actividad_economica_independiente', ''),
            'sector_economico': form_data.get('sector_economico'),
            'tiempo_desarrollo_actividad': int(form_data.get('tiempo_desarrollo_actividad', 0)),
            'tiempo_en_actividad': int(form_data.get('tiempo_en_actividad', 0)),
            'nivel_estudios': form_data.get('nivel_estudios'),
            'titulo_profesional': form_data.get('titulo_profesional', ''),
            'ingreso_principal': ingreso_principal,
            'fuente_ingresos_principal': form_data.get('fuente_ingresos_principal'),
            'otros_ingresos': otros_ingresos,
            'gastos_mensuales': gastos_mensuales,
            'monto_solicitado': monto_solicitado,
            'capacidad_pago': 0,
            'ratio_endeudamiento': 0,
            'score_riesgo': 0,
            'aprobado': 0
        }
        
        # Calcular variables derivadas
        capacidad_pago, cuota_estimada, ratio_endeudamiento = calcular_variables_derivadas(datos_entrada)
        datos_entrada['capacidad_pago'] = capacidad_pago
        datos_entrada['ratio_endeudamiento'] = ratio_endeudamiento
        
        # Crear DataFrame y realizar predicción
        df_entrada = pd.DataFrame([datos_entrada])
        X_entrada = preprocessor.transform(df_entrada)
        
        # Determinar tipo de modelo y hacer predicción apropiada
        if hasattr(modelo, 'predict_proba'):
            # Modelos sklearn (Random Forest, Gradient Boosting)
            probabilidad = float(modelo.predict_proba(X_entrada)[0][1])
        else:
            # Modelo Keras (Deep Learning)
            probabilidad = float(modelo.predict(X_entrada, verbose=0)[0][0])
        
        # Determinar nivel de riesgo
        if probabilidad >= 0.75:
            nivel_riesgo = "Bajo"
            color_riesgo = "success"
        elif probabilidad >= 0.5:
            nivel_riesgo = "Medio"
            color_riesgo = "warning"
        elif probabilidad >= 0.25:
            nivel_riesgo = "Alto"
            color_riesgo = "danger"
        else:
            nivel_riesgo = "Muy Alto"
            color_riesgo = "danger"
        
        # Generar recomendaciones
        recomendaciones = []
        if probabilidad < 0.5:
            if ratio_endeudamiento > 0.5:
                recomendaciones.append("Considere reducir el monto solicitado")
            if capacidad_pago < cuota_estimada * 1.2:
                recomendaciones.append("Mejore su capacidad de pago antes de solicitar")
            if int(form_data.get('personas_a_cargo', 0)) >= 4:
                recomendaciones.append("Alto número de personas a cargo afecta la evaluación")
            if int(form_data.get('tiempo_en_actividad', 0)) < 1:
                recomendaciones.append("Mayor estabilidad laboral mejora su perfil")
        
        # Preparar resultados
        resultados = {
            'probabilidad': probabilidad,
            'aprobado': probabilidad >= 0.5,
            'nivel_riesgo': nivel_riesgo,
            'color_riesgo': color_riesgo,
            'capacidad_pago': capacidad_pago,
            'cuota_estimada': cuota_estimada,
            'ratio_endeudamiento': ratio_endeudamiento,
            'total_ingresos': ingreso_principal + otros_ingresos,
            'recomendaciones': recomendaciones,
            'datos_solicitante': {
                'nombre': f"{form_data.get('primer_nombre')} {form_data.get('primer_apellido')}",
                'edad': edad,
                'monto_solicitado': monto_solicitado,
                'plazo_meses': int(form_data.get('plazo_meses', 12))
            }
        }
        
        return render_template('resultado.html', **resultados)
        
    except Exception as e:
        print(f"Error en análisis: {e}")
        return render_template('error.html', 
                             mensaje=f"Error al procesar la solicitud: {str(e)}")

@main.route('/api/analizar', methods=['POST'])
def api_analizar():
    """API endpoint para predicciones JSON"""
    if not cargar_modelo():
        return jsonify({'error': 'Modelo no disponible'}), 500
    
    try:
        datos = request.get_json()
        
        # Crear DataFrame y realizar predicción
        df_entrada = pd.DataFrame([datos])
        X_entrada = preprocessor.transform(df_entrada)
        probabilidad = float(modelo.predict(X_entrada, verbose=0)[0][0])
        
        return jsonify({
            'probabilidad': probabilidad,
            'aprobado': probabilidad >= 0.5,
            'nivel_riesgo': 'Bajo' if probabilidad >= 0.75 else 'Medio' if probabilidad >= 0.5 else 'Alto'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
