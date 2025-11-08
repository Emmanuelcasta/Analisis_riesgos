"""
Script de prueba del modelo de préstamos entrenado
Permite verificar predicciones con casos de ejemplo
"""
import pandas as pd
import numpy as np
import pickle
import json
from tensorflow import keras

def cargar_modelo_y_preprocessor():
    """Carga el modelo entrenado y el preprocesador"""
    import os
    print("📂 Cargando modelo y preprocesador...")
    
    models_dir = os.path.join(os.path.dirname(__file__), '..', 'models')
    
    # Cargar modelo
    modelo_path = os.path.join(models_dir, 'modelo_prestamos_final.h5')
    modelo = keras.models.load_model(modelo_path)
    print("   ✓ Modelo cargado")
    
    # Cargar preprocesador
    preprocessor_path = os.path.join(models_dir, 'preprocessor.pkl')
    with open(preprocessor_path, 'rb') as f:
        preprocessor = pickle.load(f)
    print("   ✓ Preprocesador cargado")
    
    # Cargar métricas
    metricas_path = os.path.join(models_dir, 'metricas_modelo.json')
    with open(metricas_path, 'r') as f:
        metricas = json.load(f)
    
    print(f"\n📊 Información del modelo:")
    print(f"   Fecha entrenamiento: {metricas['fecha_entrenamiento']}")
    print(f"   Accuracy: {metricas['accuracy']:.4f}")
    print(f"   AUC-ROC: {metricas['auc_roc']:.4f}")
    
    return modelo, preprocessor

def crear_caso_prueba(caso_nombre, **datos):
    """Crea un DataFrame con un caso de prueba"""
    # Valores por defecto
    default_values = {
        'tipo_documento': 'Cédula de Ciudadanía',
        'documento_identidad': 1234567890,
        'primer_nombre': 'Juan',
        'segundo_nombre': 'Carlos',
        'primer_apellido': 'Pérez',
        'segundo_apellido': 'González',
        'celular': '3001234567',
        'correo_electronico': 'test@email.com',
        'pais_residencia': 'Colombia',
        'departamento_residencia': 'Cundinamarca',
        'ciudad_residencia': 'Bogotá',
        'direccion_residencia': 'Calle 123 #45-67',
        'es_arrendador': False,
        'años_domicilio': 5,
        'fecha_nacimiento': '1985-05-15',
        'pais_nacimiento': 'Colombia',
        'departamento_nacimiento': 'Cundinamarca',
        'ciudad_nacimiento': 'Bogotá',
        'fecha_expedicion_documento': '2003-05-15',
        'pais_expedicion': 'Colombia',
        'departamento_expedicion': 'Cundinamarca',
        'ciudad_expedicion': 'Bogotá',
        'linea_credito': 'Consumo',
        'plazo_meses': 24,
        'edad': 38,
        'estado_civil': 'Casado',
        'personas_a_cargo': 2,
        'genero': 'Masculino',
        'ocupacion': 'Empleado administrativo',
        'cargo_empleado': 'Analista',
        'tipo_contrato': 'Indefinido',
        'fecha_ingreso_empresa': '2018-01-15',
        'actividad_economica_independiente': '',
        'sector_economico': 'Servicios profesionales',
        'tiempo_desarrollo_actividad': 10,
        'tiempo_en_actividad': 5,
        'nivel_estudios': 'Profesional',
        'titulo_profesional': 'Ingeniero',
        'ingreso_principal': 3000000,
        'fuente_ingresos_principal': 'Salario',
        'otros_ingresos': 0,
        'gastos_mensuales': 1800000,
        'monto_solicitado': 10000000,
        'capacidad_pago': 0,
        'ratio_endeudamiento': 0,
        'score_riesgo': 0,
        'aprobado': 0
    }
    
    # Actualizar con datos proporcionados
    default_values.update(datos)
    
    # Calcular variables derivadas
    capacidad_pago = default_values['ingreso_principal'] + default_values['otros_ingresos'] - default_values['gastos_mensuales']
    cuota_estimada = default_values['monto_solicitado'] * 0.025
    ratio_endeudamiento = cuota_estimada / (default_values['ingreso_principal'] + default_values['otros_ingresos'])
    
    default_values['capacidad_pago'] = capacidad_pago
    default_values['ratio_endeudamiento'] = ratio_endeudamiento
    
    return caso_nombre, pd.DataFrame([default_values])

def predecir_caso(modelo, preprocessor, caso_nombre, df_caso):
    """Realiza predicción para un caso específico"""
    print(f"\n{'='*70}")
    print(f"🔍 CASO: {caso_nombre}")
    print(f"{'='*70}")
    
    # Mostrar información relevante
    print(f"\n📋 Información del solicitante:")
    print(f"   Edad: {df_caso['edad'].values[0]} años")
    print(f"   Ocupación: {df_caso['ocupacion'].values[0]}")
    print(f"   Tipo contrato: {df_caso['tipo_contrato'].values[0]}")
    print(f"   Nivel estudios: {df_caso['nivel_estudios'].values[0]}")
    print(f"   Estado civil: {df_caso['estado_civil'].values[0]}")
    print(f"   Personas a cargo: {df_caso['personas_a_cargo'].values[0]}")
    
    print(f"\n💰 Información financiera:")
    print(f"   Ingreso principal: ${df_caso['ingreso_principal'].values[0]:,.0f}")
    print(f"   Otros ingresos: ${df_caso['otros_ingresos'].values[0]:,.0f}")
    print(f"   Gastos mensuales: ${df_caso['gastos_mensuales'].values[0]:,.0f}")
    print(f"   Capacidad de pago: ${df_caso['capacidad_pago'].values[0]:,.0f}")
    
    print(f"\n📊 Solicitud de crédito:")
    print(f"   Línea: {df_caso['linea_credito'].values[0]}")
    print(f"   Monto solicitado: ${df_caso['monto_solicitado'].values[0]:,.0f}")
    print(f"   Plazo: {df_caso['plazo_meses'].values[0]} meses")
    print(f"   Ratio endeudamiento: {df_caso['ratio_endeudamiento'].values[0]:.2%}")
    
    # Preprocesar y predecir
    X_caso = preprocessor.transform(df_caso)
    probabilidad = modelo.predict(X_caso, verbose=0)[0][0]
    decision = "✅ APROBADO" if probabilidad >= 0.5 else "❌ RECHAZADO"
    
    print(f"\n{'='*70}")
    print(f"🎯 RESULTADO DE LA PREDICCIÓN")
    print(f"{'='*70}")
    print(f"   Probabilidad de aprobación: {probabilidad:.2%}")
    print(f"   Decisión: {decision}")
    
    # Interpretación
    if probabilidad >= 0.75:
        nivel_riesgo = "Bajo ⭐⭐⭐"
    elif probabilidad >= 0.5:
        nivel_riesgo = "Medio ⭐⭐"
    elif probabilidad >= 0.25:
        nivel_riesgo = "Alto ⭐"
    else:
        nivel_riesgo = "Muy Alto ⚠️"
    
    print(f"   Nivel de riesgo: {nivel_riesgo}")
    
    # Recomendaciones
    print(f"\n💡 Análisis:")
    if probabilidad >= 0.5:
        print("   ✓ El perfil cumple con los criterios de aprobación")
        print("   ✓ Capacidad de pago adecuada")
        print("   ✓ Ratio de endeudamiento dentro de límites aceptables")
    else:
        print("   • El perfil presenta factores de riesgo elevados")
        if df_caso['ratio_endeudamiento'].values[0] > 0.5:
            print("   • Ratio de endeudamiento muy alto (>50%)")
        if df_caso['capacidad_pago'].values[0] < df_caso['monto_solicitado'].values[0] * 0.03:
            print("   • Capacidad de pago insuficiente")
        if df_caso['personas_a_cargo'].values[0] >= 4:
            print("   • Alto número de personas a cargo")
    
    return probabilidad, decision

def ejecutar_pruebas():
    """Ejecuta batería de pruebas con casos diversos"""
    print("="*70)
    print("🧪 PRUEBAS DEL MODELO DE ANÁLISIS DE PRÉSTAMOS")
    print("="*70)
    
    # Cargar modelo
    modelo, preprocessor = cargar_modelo_y_preprocessor()
    
    # Definir casos de prueba
    casos = []
    
    # CASO 1: Perfil ideal - Alta probabilidad de aprobación
    casos.append(crear_caso_prueba(
        "Perfil Ideal - Profesional Estable",
        edad=35,
        ocupacion='Ingeniero',
        tipo_contrato='Indefinido',
        nivel_estudios='Profesional',
        titulo_profesional='Ingeniero de Sistemas',
        ingreso_principal=5000000,
        otros_ingresos=500000,
        gastos_mensuales=2500000,
        monto_solicitado=15000000,
        plazo_meses=36,
        personas_a_cargo=1,
        estado_civil='Casado',
        es_arrendador=True,
        años_domicilio=5
    ))
    
    # CASO 2: Perfil medio - Independiente con buenos ingresos
    casos.append(crear_caso_prueba(
        "Independiente - Comerciante Establecido",
        edad=42,
        ocupacion='Comerciante',
        tipo_contrato='Independiente',
        actividad_economica_independiente='Tienda de barrio',
        sector_economico='Comercio al por menor',
        nivel_estudios='Bachillerato',
        ingreso_principal=3500000,
        otros_ingresos=800000,
        gastos_mensuales=2200000,
        monto_solicitado=12000000,
        plazo_meses=24,
        personas_a_cargo=2,
        años_domicilio=10,
        tiempo_desarrollo_actividad=8
    ))
    
    # CASO 3: Perfil riesgoso - Alto endeudamiento
    casos.append(crear_caso_prueba(
        "Alto Riesgo - Endeudamiento Elevado",
        edad=28,
        ocupacion='Vendedor',
        tipo_contrato='Fijo',
        nivel_estudios='Técnico',
        ingreso_principal=1800000,
        otros_ingresos=0,
        gastos_mensuales=1500000,
        monto_solicitado=10000000,
        plazo_meses=60,
        personas_a_cargo=3,
        estado_civil='Unión Libre',
        años_domicilio=1
    ))
    
    # CASO 4: Joven profesional - Recién graduado
    casos.append(crear_caso_prueba(
        "Joven Profesional - Primer Empleo",
        edad=24,
        ocupacion='Profesional independiente',
        tipo_contrato='Prestación de Servicios',
        nivel_estudios='Profesional',
        titulo_profesional='Administrador de Empresas',
        ingreso_principal=2500000,
        otros_ingresos=0,
        gastos_mensuales=1600000,
        monto_solicitado=8000000,
        plazo_meses=24,
        personas_a_cargo=0,
        estado_civil='Soltero',
        años_domicilio=2
    ))
    
    # CASO 5: Microempresario rural
    casos.append(crear_caso_prueba(
        "Microempresario Rural - Agricultura",
        edad=50,
        ocupacion='Agricultor',
        tipo_contrato='Independiente',
        actividad_economica_independiente='Agricultura familiar',
        sector_economico='Agricultura y ganadería',
        nivel_estudios='Primaria',
        ingreso_principal=1500000,
        otros_ingresos=400000,
        gastos_mensuales=1100000,
        monto_solicitado=5000000,
        plazo_meses=18,
        personas_a_cargo=2,
        años_domicilio=20,
        tiempo_desarrollo_actividad=15,
        ciudad_residencia='Villavicencio'
    ))
    
    # Ejecutar predicciones
    resultados = []
    for caso_nombre, df_caso in casos:
        prob, decision = predecir_caso(modelo, preprocessor, caso_nombre, df_caso)
        resultados.append({
            'caso': caso_nombre,
            'probabilidad': prob,
            'decision': decision
        })
    
    # Resumen final
    print(f"\n{'='*70}")
    print("📊 RESUMEN DE PRUEBAS")
    print(f"{'='*70}\n")
    
    for res in resultados:
        print(f"   {res['caso']}")
        print(f"      → Probabilidad: {res['probabilidad']:.2%} | {res['decision']}")
    
    aprobados = sum(1 for r in resultados if "APROBADO" in r['decision'])
    print(f"\n   Total casos probados: {len(resultados)}")
    print(f"   Aprobados: {aprobados} | Rechazados: {len(resultados) - aprobados}")
    
    print(f"\n{'='*70}")
    print("✅ PRUEBAS COMPLETADAS EXITOSAMENTE")
    print(f"{'='*70}\n")

if __name__ == '__main__':
    ejecutar_pruebas()
