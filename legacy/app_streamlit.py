"""
Interfaz de usuario para el sistema de análisis de préstamos
Permite a los usuarios ingresar sus datos y recibir análisis en tiempo real
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from datetime import datetime, date
from tensorflow import keras
import plotly.graph_objects as go
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Sistema de Análisis de Préstamos",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .danger-box {
        background-color: #f8d7da;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #dc3545;
        margin: 1rem 0;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def cargar_modelo():
    """Carga el modelo y preprocesador (con caché)"""
    try:
        modelo = keras.models.load_model('modelo_prestamos_final.h5')
        with open('preprocessor.pkl', 'rb') as f:
            preprocessor = pickle.load(f)
        with open('metricas_modelo.json', 'r') as f:
            metricas = json.load(f)
        return modelo, preprocessor, metricas
    except Exception as e:
        st.error(f"Error al cargar el modelo: {e}")
        return None, None, None

def calcular_variables_derivadas(datos):
    """Calcula variables derivadas de los datos ingresados"""
    capacidad_pago = datos['ingreso_principal'] + datos['otros_ingresos'] - datos['gastos_mensuales']
    cuota_estimada = datos['monto_solicitado'] * 0.025  # Estimación simplificada
    
    total_ingresos = datos['ingreso_principal'] + datos['otros_ingresos']
    ratio_endeudamiento = cuota_estimada / total_ingresos if total_ingresos > 0 else 1
    
    return capacidad_pago, cuota_estimada, ratio_endeudamiento

def crear_gauge_probabilidad(probabilidad):
    """Crea un gráfico de gauge para la probabilidad"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probabilidad * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Probabilidad de Aprobación", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "green"}},
        gauge={
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 25], 'color': '#ffcccc'},
                {'range': [25, 50], 'color': '#ffe6cc'},
                {'range': [50, 75], 'color': '#ccffcc'},
                {'range': [75, 100], 'color': '#99ff99'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig

def main():
    # Encabezado
    st.markdown('<div class="main-header">💰 Sistema de Análisis de Préstamos con IA</div>', unsafe_allow_html=True)
    st.markdown('<div class="info-box">Sistema inteligente para evaluación de solicitudes de crédito. Complete todos los campos para recibir un análisis personalizado.</div>', unsafe_allow_html=True)
    
    # Cargar modelo
    modelo, preprocessor, metricas = cargar_modelo()
    
    if modelo is None:
        st.error("⚠️ No se pudo cargar el modelo. Asegúrese de haber entrenado el modelo primero ejecutando `entrenar_modelo.py`")
        return
    
    # Sidebar con información del modelo
    with st.sidebar:
        st.markdown("### 📊 Información del Modelo")
        st.metric("Accuracy", f"{metricas['accuracy']:.2%}")
        st.metric("AUC-ROC", f"{metricas['auc_roc']:.3f}")
        st.metric("Fecha entrenamiento", metricas['fecha_entrenamiento'][:10])
        
        st.markdown("---")
        st.markdown("### ℹ️ Acerca del Sistema")
        st.info("""
        Este sistema utiliza inteligencia artificial para analizar solicitudes de préstamos, 
        considerando múltiples factores como:
        - Capacidad de pago
        - Estabilidad laboral
        - Nivel de ingresos
        - Perfil demográfico
        - Historial de residencia
        """)
    
    # Formulario principal
    st.markdown('<div class="sub-header">📝 Paso 1: Datos Generales</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tipo_documento = st.selectbox("Tipo de documento", 
            ['Cédula de Ciudadanía', 'Cédula de Extranjería', 'Pasaporte'])
        documento_identidad = st.text_input("Número de documento", "1234567890")
        primer_nombre = st.text_input("Primer nombre", "Juan")
        segundo_nombre = st.text_input("Segundo nombre (opcional)", "Carlos")
        primer_apellido = st.text_input("Primer apellido", "Pérez")
        segundo_apellido = st.text_input("Segundo apellido", "González")
    
    with col2:
        celular = st.text_input("Celular", "3001234567")
        correo_electronico = st.text_input("Correo electrónico", "usuario@email.com")
        departamento_residencia = st.selectbox("Departamento de residencia",
            ['Cundinamarca', 'Antioquia', 'Valle del Cauca', 'Atlántico', 'Santander', 
             'Bolívar', 'Boyacá', 'Caldas', 'Otro'])
        ciudad_residencia = st.selectbox("Ciudad de residencia",
            ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Bucaramanga', 
             'Cúcuta', 'Pereira', 'Ibagué', 'Manizales', 'Otra'])
        direccion_residencia = st.text_input("Dirección de residencia", "Calle 123 #45-67")
    
    with col3:
        es_arrendador = st.checkbox("¿Es propietario de la vivienda?")
        años_domicilio = st.number_input("¿Cuántos años vive en su domicilio?", 0, 50, 5)
        fecha_nacimiento = st.date_input("Fecha de nacimiento", 
            value=date(1985, 5, 15), min_value=date(1940, 1, 1), max_value=date(2006, 12, 31))
        edad = datetime.now().year - fecha_nacimiento.year
        st.info(f"Edad calculada: {edad} años")
        
        linea_credito = st.selectbox("Línea de crédito", 
            ['Consumo', 'Libre Inversión', 'Microcrédito', 'Vehículo', 'Vivienda'])
        plazo_meses = st.selectbox("Plazo (meses)", [6, 12, 18, 24, 36, 48, 60])
    
    st.markdown('<div class="sub-header">👤 Paso 2: Información Personal y Laboral</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        estado_civil = st.selectbox("Estado civil", 
            ['Soltero', 'Casado', 'Unión Libre', 'Divorciado', 'Viudo'])
        personas_a_cargo = st.number_input("Personas a cargo", 0, 10, 2)
        genero = st.selectbox("Género", ['Masculino', 'Femenino', 'Otro'])
        nivel_estudios = st.selectbox("Nivel de estudios",
            ['Primaria', 'Bachillerato', 'Técnico', 'Tecnólogo', 'Profesional', 'Posgrado'])
        titulo_profesional = st.text_input("Título profesional (si aplica)", "")
    
    with col2:
        ocupacion = st.selectbox("Ocupación",
            ['Empleado administrativo', 'Comerciante', 'Profesional independiente', 
             'Agricultor', 'Conductor', 'Técnico', 'Operario', 'Vendedor', 'Otro'])
        cargo_empleado = st.text_input("Cargo del empleado", "Analista")
        tipo_contrato = st.selectbox("Tipo de contrato",
            ['Indefinido', 'Fijo', 'Obra o Labor', 'Prestación de Servicios', 'Independiente'])
        sector_economico = st.selectbox("Sector económico",
            ['Servicios profesionales', 'Comercio al por menor', 'Comercio al por mayor',
             'Tecnología', 'Salud', 'Educación', 'Construcción', 'Manufactura', 
             'Agricultura y ganadería', 'Transporte', 'Otro'])
    
    with col3:
        actividad_economica_independiente = st.text_input(
            "Actividad económica (si es independiente)", "")
        tiempo_desarrollo_actividad = st.number_input(
            "Años de experiencia en la actividad", 0, 50, 10)
        tiempo_en_actividad = st.number_input(
            "Años en la actividad actual", 0, 50, 5)
        fuente_ingresos_principal = st.selectbox(
            "Fuente principal de ingresos", ['Salario', 'Negocio propio', 'Honorarios', 'Otro'])
    
    st.markdown('<div class="sub-header">💵 Paso 3: Información Financiera</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        ingreso_principal = st.number_input("Ingreso principal mensual ($COP)", 
            0, 100000000, 3000000, step=100000)
        otros_ingresos = st.number_input("Otros ingresos mensuales ($COP)", 
            0, 50000000, 0, step=100000)
        total_ingresos = ingreso_principal + otros_ingresos
        st.success(f"**Total ingresos:** ${total_ingresos:,.0f}")
    
    with col2:
        gastos_mensuales = st.number_input("Gastos mensuales ($COP)", 
            0, 100000000, 1800000, step=100000)
        monto_solicitado = st.number_input("Monto del préstamo solicitado ($COP)", 
            500000, 100000000, 10000000, step=500000)
        st.info(f"**Capacidad de pago:** ${max(0, total_ingresos - gastos_mensuales):,.0f}")
    
    # Botón de análisis
    st.markdown("---")
    
    if st.button("🔍 Analizar Solicitud", type="primary", use_container_width=True):
        
        # Preparar datos
        datos_entrada = {
            'tipo_documento': tipo_documento,
            'documento_identidad': int(documento_identidad) if documento_identidad.isdigit() else 0,
            'primer_nombre': primer_nombre,
            'segundo_nombre': segundo_nombre,
            'primer_apellido': primer_apellido,
            'segundo_apellido': segundo_apellido,
            'celular': celular,
            'correo_electronico': correo_electronico,
            'pais_residencia': 'Colombia',
            'departamento_residencia': departamento_residencia,
            'ciudad_residencia': ciudad_residencia,
            'direccion_residencia': direccion_residencia,
            'es_arrendador': es_arrendador,
            'años_domicilio': años_domicilio,
            'fecha_nacimiento': fecha_nacimiento,
            'pais_nacimiento': 'Colombia',
            'departamento_nacimiento': departamento_residencia,
            'ciudad_nacimiento': ciudad_residencia,
            'fecha_expedicion_documento': fecha_nacimiento,
            'pais_expedicion': 'Colombia',
            'departamento_expedicion': departamento_residencia,
            'ciudad_expedicion': ciudad_residencia,
            'linea_credito': linea_credito,
            'plazo_meses': plazo_meses,
            'edad': edad,
            'estado_civil': estado_civil,
            'personas_a_cargo': personas_a_cargo,
            'genero': genero,
            'ocupacion': ocupacion,
            'cargo_empleado': cargo_empleado,
            'tipo_contrato': tipo_contrato,
            'fecha_ingreso_empresa': datetime.now(),
            'actividad_economica_independiente': actividad_economica_independiente,
            'sector_economico': sector_economico,
            'tiempo_desarrollo_actividad': tiempo_desarrollo_actividad,
            'tiempo_en_actividad': tiempo_en_actividad,
            'nivel_estudios': nivel_estudios,
            'titulo_profesional': titulo_profesional,
            'ingreso_principal': ingreso_principal,
            'fuente_ingresos_principal': fuente_ingresos_principal,
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
        
        # Crear DataFrame
        df_entrada = pd.DataFrame([datos_entrada])
        
        # Realizar predicción
        with st.spinner("🤖 Analizando su solicitud con inteligencia artificial..."):
            X_entrada = preprocessor.transform(df_entrada)
            probabilidad = modelo.predict(X_entrada, verbose=0)[0][0]
        
        # Mostrar resultados
        st.markdown('<div class="sub-header">📊 Resultados del Análisis</div>', unsafe_allow_html=True)
        
        # Gauge de probabilidad
        col1, col2 = st.columns([2, 3])
        
        with col1:
            fig_gauge = crear_gauge_probabilidad(probabilidad)
            st.plotly_chart(fig_gauge, use_container_width=True)
        
        with col2:
            # Decisión
            if probabilidad >= 0.5:
                st.markdown(f"""
                <div class="success-box">
                    <h2>✅ SOLICITUD APROBADA</h2>
                    <p style="font-size: 1.2rem;">Su solicitud ha sido <strong>aprobada</strong> con una probabilidad del <strong>{probabilidad*100:.1f}%</strong></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="danger-box">
                    <h2>❌ SOLICITUD RECHAZADA</h2>
                    <p style="font-size: 1.2rem;">Su solicitud ha sido <strong>rechazada</strong>. Probabilidad de aprobación: <strong>{probabilidad*100:.1f}%</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            # Nivel de riesgo
            if probabilidad >= 0.75:
                nivel_riesgo = "Bajo ⭐⭐⭐"
                color_riesgo = "green"
            elif probabilidad >= 0.5:
                nivel_riesgo = "Medio ⭐⭐"
                color_riesgo = "orange"
            elif probabilidad >= 0.25:
                nivel_riesgo = "Alto ⭐"
                color_riesgo = "red"
            else:
                nivel_riesgo = "Muy Alto ⚠️"
                color_riesgo = "darkred"
            
            st.markdown(f"**Nivel de Riesgo:** <span style='color: {color_riesgo}; font-size: 1.3rem; font-weight: bold;'>{nivel_riesgo}</span>", 
                       unsafe_allow_html=True)
        
        # Métricas financieras
        st.markdown("### 💰 Análisis Financiero Detallado")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Ingresos Totales", f"${total_ingresos:,.0f}", 
                     delta=f"${otros_ingresos:,.0f} otros" if otros_ingresos > 0 else "Sin otros ingresos")
        
        with col2:
            st.metric("Gastos Mensuales", f"${gastos_mensuales:,.0f}",
                     delta=f"{(gastos_mensuales/total_ingresos*100):.1f}% de ingresos")
        
        with col3:
            st.metric("Capacidad de Pago", f"${capacidad_pago:,.0f}",
                     delta="Positiva" if capacidad_pago > 0 else "Negativa",
                     delta_color="normal" if capacidad_pago > 0 else "inverse")
        
        with col4:
            st.metric("Ratio Endeudamiento", f"{ratio_endeudamiento*100:.1f}%",
                     delta="Aceptable" if ratio_endeudamiento <= 0.4 else "Alto",
                     delta_color="normal" if ratio_endeudamiento <= 0.4 else "inverse")
        
        # Detalles del préstamo
        st.markdown("### 📋 Detalles del Préstamo")
        col1, col2 = st.columns(2)
        
        with col1:
            st.info(f"""
            **Monto Solicitado:** ${monto_solicitado:,.0f}  
            **Plazo:** {plazo_meses} meses  
            **Cuota Estimada:** ${cuota_estimada:,.0f}/mes  
            **Tasa Estimada:** 2.5% mensual
            """)
        
        with col2:
            # Recomendaciones
            st.markdown("**💡 Recomendaciones:**")
            if probabilidad >= 0.5:
                st.success("""
                ✓ Perfil cumple con criterios de aprobación  
                ✓ Capacidad de pago adecuada  
                ✓ Ratio de endeudamiento aceptable
                """)
            else:
                recomendaciones = []
                if ratio_endeudamiento > 0.5:
                    recomendaciones.append("• Considere reducir el monto solicitado")
                if capacidad_pago < cuota_estimada * 1.2:
                    recomendaciones.append("• Mejore su capacidad de pago antes de solicitar")
                if personas_a_cargo >= 4:
                    recomendaciones.append("• Alto número de personas a cargo afecta evaluación")
                if tiempo_en_actividad < 1:
                    recomendaciones.append("• Mayor estabilidad laboral mejora su perfil")
                
                st.warning("\n".join(recomendaciones) if recomendaciones else "Consulte con un asesor financiero")
        
        # Gráfico de distribución de ingresos y gastos
        st.markdown("### 📊 Distribución Financiera")
        
        fig_finanzas = go.Figure(data=[
            go.Bar(name='Ingresos', x=['Financiero'], y=[total_ingresos], marker_color='green'),
            go.Bar(name='Gastos', x=['Financiero'], y=[gastos_mensuales], marker_color='red'),
            go.Bar(name='Cuota Préstamo', x=['Financiero'], y=[cuota_estimada], marker_color='orange')
        ])
        
        fig_finanzas.update_layout(
            title="Comparación: Ingresos vs Gastos vs Cuota",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig_finanzas, use_container_width=True)

if __name__ == '__main__':
    main()
