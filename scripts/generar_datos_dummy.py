"""
Generador de datos dummy para entrenamiento del modelo de préstamos
"""
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('es_CO')  # Español de Colombia
np.random.seed(42)
random.seed(42)

# Definir opciones para campos categóricos
TIPOS_DOCUMENTO = ['Cédula de Ciudadanía', 'Cédula de Extranjería', 'Pasaporte']
ESTADOS_CIVIL = ['Soltero', 'Casado', 'Unión Libre', 'Divorciado', 'Viudo']
GENEROS = ['Masculino', 'Femenino', 'Otro']
TIPOS_CONTRATO = ['Indefinido', 'Fijo', 'Obra o Labor', 'Prestación de Servicios', 'Independiente']
NIVELES_ESTUDIO = ['Primaria', 'Bachillerato', 'Técnico', 'Tecnólogo', 'Profesional', 'Posgrado']
LINEAS_CREDITO = ['Consumo', 'Libre Inversión', 'Vehículo', 'Vivienda', 'Microcrédito']

SECTORES_ECONOMICOS = [
    'Agricultura y ganadería', 'Comercio al por menor', 'Comercio al por mayor',
    'Construcción', 'Educación', 'Manufactura', 'Salud', 'Servicios profesionales',
    'Tecnología', 'Transporte', 'Turismo y hotelería', 'Otro'
]

ACTIVIDADES_INDEPENDIENTE = [
    'Tienda de barrio', 'Restaurante', 'Transporte público', 'Construcción',
    'Servicios de belleza', 'Agricultura familiar', 'Comercio ambulante',
    'Artesanías', 'Reparación y mantenimiento', 'Consultoría'
]

OCUPACIONES = [
    'Comerciante', 'Conductor', 'Agricultor', 'Obrero', 'Empleado administrativo',
    'Profesional independiente', 'Técnico', 'Vendedor', 'Operario', 'Docente',
    'Enfermero', 'Ingeniero', 'Contador', 'Otro'
]

CIUDADES_COLOMBIA = [
    'Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 'Cúcuta',
    'Bucaramanga', 'Pereira', 'Santa Marta', 'Ibagué', 'Manizales', 'Villavicencio'
]

DEPARTAMENTOS = [
    'Antioquia', 'Atlántico', 'Bolívar', 'Boyacá', 'Caldas', 'Cauca', 'Cesar',
    'Córdoba', 'Cundinamarca', 'Huila', 'La Guajira', 'Magdalena', 'Meta',
    'Nariño', 'Norte de Santander', 'Quindío', 'Risaralda', 'Santander',
    'Tolima', 'Valle del Cauca'
]

def generar_fecha_nacimiento(edad):
    """Genera fecha de nacimiento coherente con la edad"""
    hoy = datetime.now()
    año_nacimiento = hoy.year - edad
    return fake.date_between(
        start_date=datetime(año_nacimiento, 1, 1),
        end_date=datetime(año_nacimiento, 12, 31)
    )

def generar_datos(n_samples=10000):
    """Genera dataset completo con todas las variables del formulario"""
    datos = []
    
    for i in range(n_samples):
        # Paso 1: Datos Generales
        tipo_documento = random.choice(TIPOS_DOCUMENTO)
        documento = fake.random_number(digits=10, fix_len=True)
        primer_nombre = fake.first_name()
        segundo_nombre = fake.first_name() if random.random() > 0.3 else ''
        primer_apellido = fake.last_name()
        segundo_apellido = fake.last_name()
        celular = f"3{fake.random_number(digits=9, fix_len=True)}"
        email = fake.email()
        
        # Residencia
        pais_residencia = 'Colombia'
        departamento_residencia = random.choice(DEPARTAMENTOS)
        ciudad_residencia = random.choice(CIUDADES_COLOMBIA)
        direccion_residencia = fake.address().replace('\n', ', ')
        es_arrendador = random.choice([True, False])
        años_domicilio = np.random.randint(0, 31)  # 0 a 30 años
        
        # Nacimiento - Usar rango más amplio para evitar problemas
        edad = np.random.randint(20, 70)  # Rango más seguro
        fecha_nacimiento = generar_fecha_nacimiento(edad)
        pais_nacimiento = 'Colombia' if random.random() > 0.1 else fake.country()
        departamento_nacimiento = random.choice(DEPARTAMENTOS)
        ciudad_nacimiento = random.choice(CIUDADES_COLOMBIA)
        
        # Documento
        fecha_expedicion = fake.date_between(
            start_date=fecha_nacimiento + timedelta(days=6570),  # +18 años
            end_date=datetime.now()
        )
        pais_expedicion = 'Colombia'
        departamento_expedicion = random.choice(DEPARTAMENTOS)
        ciudad_expedicion = random.choice(CIUDADES_COLOMBIA)
        
        # Crédito
        linea_credito = random.choice(LINEAS_CREDITO)
        monto_solicitado = np.random.randint(500000, 50000000)  # $500K - $50M COP
        plazo_meses = random.choice([6, 12, 18, 24, 36, 48, 60])
        
        # Paso 2: Conocimiento
        estado_civil = random.choice(ESTADOS_CIVIL)
        personas_a_cargo = np.random.randint(0, 7)  # 0 a 6 personas
        genero = random.choice(GENEROS)
        ocupacion = random.choice(OCUPACIONES)
        cargo_empleado = fake.job() if ocupacion == 'Empleado administrativo' else ''
        tipo_contrato = random.choice(TIPOS_CONTRATO)
        
        # Fecha ingreso empresa (coherente con edad y experiencia)
        max_años = max(edad - 18, 1)  # Asegurar que sea al menos 1
        años_empresa = min(np.random.randint(0, max_años + 1), 30)
        fecha_ingreso = datetime.now() - timedelta(days=años_empresa*365)
        
        # Actividad económica
        if tipo_contrato == 'Independiente':
            actividad_independiente = random.choice(ACTIVIDADES_INDEPENDIENTE)
            sector_economico = random.choice(SECTORES_ECONOMICOS)
        else:
            actividad_independiente = ''
            sector_economico = random.choice(SECTORES_ECONOMICOS)
        
        # Tiempo de desarrollo de actividad (asegurar valores válidos)
        max_tiempo_desarrollo = max(min(edad - 17, 30), 1)
        tiempo_desarrollo_actividad = np.random.randint(1, max_tiempo_desarrollo + 1)
        tiempo_en_actividad = np.random.randint(1, tiempo_desarrollo_actividad + 1)
        nivel_estudios = random.choice(NIVELES_ESTUDIO)
        titulo_profesional = fake.job() if nivel_estudios in ['Profesional', 'Posgrado'] else ''
        
        # Ingresos y gastos (coherentes con ocupación y edad)
        # Aumentamos variabilidad para generar más casos de rechazo
        if tipo_contrato == 'Independiente':
            ingreso_base = np.random.randint(800000, 5000000)
        elif nivel_estudios in ['Profesional', 'Posgrado']:
            ingreso_base = np.random.randint(2000000, 10000000)
        else:
            ingreso_base = np.random.randint(1300000, 4000000)
        
        ingreso_principal = int(ingreso_base * np.random.uniform(0.9, 1.1))
        fuente_ingresos = 'Salario' if tipo_contrato != 'Independiente' else 'Negocio propio'
        otros_ingresos = int(np.random.uniform(0, 1000000)) if random.random() > 0.6 else 0
        
        # Gastos más variados para generar casos de rechazo
        # 40% de casos con gastos altos (potencial rechazo)
        if random.random() < 0.4:
            gastos_mensuales = int(ingreso_principal * np.random.uniform(0.55, 0.90))  # Gastos altos
        else:
            gastos_mensuales = int(ingreso_principal * np.random.uniform(0.30, 0.60))  # Gastos normales
        
        # ============================================================
        # CRITERIOS DE DECISIÓN - REGLAS DE NEGOCIO ESTRICTAS
        # ============================================================
        
        # Calculamos variables derivadas para el scoring
        total_ingresos = ingreso_principal + otros_ingresos
        capacidad_pago = total_ingresos - gastos_mensuales
        
        # Cálculo realista de la cuota mensual usando fórmula de amortización
        # Tasas de interés mensuales según línea de crédito (realistas para Colombia)
        tasas_interes_mensual = {
            'Consumo': 0.025,          # ~30% EA (2.5% mensual)
            'Libre Inversión': 0.022,  # ~26% EA (2.2% mensual)
            'Vehículo': 0.018,         # ~22% EA (1.8% mensual)
            'Vivienda': 0.010,         # ~12% EA (1.0% mensual)
            'Microcrédito': 0.030      # ~36% EA (3.0% mensual)
        }
        
        tasa_mensual = tasas_interes_mensual.get(linea_credito, 0.022)
        
        # Fórmula de cuota: C = P * [i * (1 + i)^n] / [(1 + i)^n - 1]
        # Donde: P = monto, i = tasa mensual, n = plazo en meses
        if tasa_mensual > 0:
            factor = (1 + tasa_mensual) ** plazo_meses
            cuota_estimada = monto_solicitado * (tasa_mensual * factor) / (factor - 1)
        else:
            cuota_estimada = monto_solicitado / plazo_meses
        
        ratio_gastos_ingresos = gastos_mensuales / total_ingresos if total_ingresos > 0 else 1
        ratio_endeudamiento = cuota_estimada / total_ingresos if total_ingresos > 0 else 1
        ratio_capacidad_cuota = capacidad_pago / cuota_estimada if cuota_estimada > 0 else 0
        
        # CRITERIOS DE RECHAZO AUTOMÁTICO (Hard Rules)
        motivo_rechazo = []
        aprobado = 1  # Asumimos aprobación inicial
        
        # Regla 1: Gastos superiores al 60% de ingresos = RECHAZO
        if ratio_gastos_ingresos > 0.60:
            aprobado = 0
            motivo_rechazo.append("Gastos exceden 60% de ingresos")
        
        # Regla 2: Ratio de endeudamiento superior al 40% = RECHAZO
        if ratio_endeudamiento > 0.40:
            aprobado = 0
            motivo_rechazo.append("Ratio endeudamiento excede 40%")
        
        # Regla 3: Capacidad de pago insuficiente (debe poder pagar al menos 1.5x la cuota)
        if capacidad_pago < cuota_estimada * 1.5:
            aprobado = 0
            motivo_rechazo.append("Capacidad de pago insuficiente")
        
        # Regla 4: Capacidad de pago negativa = RECHAZO INMEDIATO
        if capacidad_pago <= 0:
            aprobado = 0
            motivo_rechazo.append("Capacidad de pago negativa")
        
        # Regla 5: Edad fuera de rango aceptable = RECHAZO
        if edad < 20 or edad > 65:
            aprobado = 0
            motivo_rechazo.append("Edad fuera del rango aceptable")
        
        # Regla 6: Ingresos muy bajos para el monto solicitado
        salario_minimo = 1300000
        if total_ingresos < salario_minimo or monto_solicitado > total_ingresos * 10:
            aprobado = 0
            motivo_rechazo.append("Ingresos insuficientes para el monto solicitado")
        
        # Regla 7: Contratos inestables con poco tiempo
        if tipo_contrato in ['Prestación de Servicios', 'Temporal'] and años_empresa < 1:
            aprobado = 0
            motivo_rechazo.append("Contrato inestable con poca antigüedad")
        
        # Regla 8: Demasiadas personas a cargo con ingresos bajos
        if personas_a_cargo >= 4 and total_ingresos < 3 * salario_minimo:
            aprobado = 0
            motivo_rechazo.append("Muchas personas a cargo con ingresos insuficientes")
        
        # SCORING PARA CASOS QUE PASAN LAS REGLAS DURAS
        score_riesgo = 0
        
        if aprobado == 1:  # Solo calculamos score si no fue rechazado automáticamente
            
            # Factor 1: Ratio de Endeudamiento (30 puntos)
            if ratio_endeudamiento <= 0.20:
                score_riesgo += 30
            elif ratio_endeudamiento <= 0.25:
                score_riesgo += 25
            elif ratio_endeudamiento <= 0.30:
                score_riesgo += 20
            elif ratio_endeudamiento <= 0.35:
                score_riesgo += 10
            else:
                score_riesgo += 5
            
            # Factor 2: Capacidad de Pago vs Cuota (25 puntos)
            if ratio_capacidad_cuota >= 3:
                score_riesgo += 25
            elif ratio_capacidad_cuota >= 2.5:
                score_riesgo += 20
            elif ratio_capacidad_cuota >= 2:
                score_riesgo += 15
            elif ratio_capacidad_cuota >= 1.5:
                score_riesgo += 10
            else:
                score_riesgo += 5
            
            # Factor 3: Ratio Gastos/Ingresos (20 puntos)
            if ratio_gastos_ingresos <= 0.40:
                score_riesgo += 20
            elif ratio_gastos_ingresos <= 0.50:
                score_riesgo += 15
            elif ratio_gastos_ingresos <= 0.55:
                score_riesgo += 10
            else:
                score_riesgo += 5
            
            # Factor 4: Estabilidad Laboral (15 puntos)
            if tipo_contrato == 'Indefinido' and años_empresa >= 3:
                score_riesgo += 15
            elif tipo_contrato == 'Indefinido' and años_empresa >= 1:
                score_riesgo += 12
            elif tipo_contrato == 'Fijo' and años_empresa >= 2:
                score_riesgo += 10
            elif tipo_contrato == 'Independiente' and años_empresa >= 5:
                score_riesgo += 10
            elif años_empresa >= 1:
                score_riesgo += 5
            else:
                score_riesgo += 2
            
            # Factor 5: Nivel de Ingresos (10 puntos)
            if total_ingresos >= 5 * salario_minimo:
                score_riesgo += 10
            elif total_ingresos >= 4 * salario_minimo:
                score_riesgo += 8
            elif total_ingresos >= 3 * salario_minimo:
                score_riesgo += 6
            elif total_ingresos >= 2 * salario_minimo:
                score_riesgo += 4
            else:
                score_riesgo += 2
            
            # Bonificaciones adicionales
            if otros_ingresos > 0 and otros_ingresos >= ingreso_principal * 0.2:
                score_riesgo += 3  # Diversificación de ingresos
            
            if es_arrendador:
                score_riesgo += 2  # Propietario de vivienda
            
            if nivel_estudios in ['Profesional', 'Posgrado']:
                score_riesgo += 2  # Nivel educativo alto
            
            if 28 <= edad <= 55:
                score_riesgo += 3  # Edad óptima
            
            # Penalizaciones
            if personas_a_cargo >= 3:
                score_riesgo -= 3
            
            if tipo_contrato in ['Prestación de Servicios', 'Temporal']:
                score_riesgo -= 5
            
            # Decisión final basada en score
            # Score >= 70: Aprobación segura
            # Score 60-69: Zona gris, depende de factores adicionales
            # Score < 60: Rechazo
            
            if score_riesgo >= 70:
                aprobado = 1
            elif score_riesgo >= 60:
                # Zona gris: 50% de probabilidad de aprobación
                aprobado = 1 if random.random() > 0.5 else 0
                if aprobado == 0:
                    motivo_rechazo.append("Score de riesgo en zona límite")
            else:
                aprobado = 0
                motivo_rechazo.append("Score de riesgo bajo (< 60)")
        
        else:
            # Si fue rechazado por reglas duras, score máximo de 50
            score_riesgo = min(random.randint(30, 55), 50)
        
        # Agregar registro
        registro = {
            # Datos Generales
            'tipo_documento': tipo_documento,
            'documento_identidad': documento,
            'primer_nombre': primer_nombre,
            'segundo_nombre': segundo_nombre,
            'primer_apellido': primer_apellido,
            'segundo_apellido': segundo_apellido,
            'celular': celular,
            'correo_electronico': email,
            'pais_residencia': pais_residencia,
            'departamento_residencia': departamento_residencia,
            'ciudad_residencia': ciudad_residencia,
            'direccion_residencia': direccion_residencia,
            'es_arrendador': es_arrendador,
            'años_domicilio': años_domicilio,
            'fecha_nacimiento': fecha_nacimiento,
            'pais_nacimiento': pais_nacimiento,
            'departamento_nacimiento': departamento_nacimiento,
            'ciudad_nacimiento': ciudad_nacimiento,
            'fecha_expedicion_documento': fecha_expedicion,
            'pais_expedicion': pais_expedicion,
            'departamento_expedicion': departamento_expedicion,
            'ciudad_expedicion': ciudad_expedicion,
            'linea_credito': linea_credito,
            'plazo_meses': plazo_meses,
            
            # Conocimiento
            'edad': edad,
            'estado_civil': estado_civil,
            'personas_a_cargo': personas_a_cargo,
            'genero': genero,
            'ocupacion': ocupacion,
            'cargo_empleado': cargo_empleado,
            'tipo_contrato': tipo_contrato,
            'fecha_ingreso_empresa': fecha_ingreso,
            'actividad_economica_independiente': actividad_independiente,
            'sector_economico': sector_economico,
            'tiempo_desarrollo_actividad': tiempo_desarrollo_actividad,
            'tiempo_en_actividad': tiempo_en_actividad,
            'nivel_estudios': nivel_estudios,
            'titulo_profesional': titulo_profesional,
            'ingreso_principal': ingreso_principal,
            'fuente_ingresos_principal': fuente_ingresos,
            'otros_ingresos': otros_ingresos,
            'gastos_mensuales': gastos_mensuales,
            'monto_solicitado': monto_solicitado,
            
            # Variables derivadas
            'capacidad_pago': capacidad_pago,
            'ratio_endeudamiento': ratio_endeudamiento,
            'score_riesgo': score_riesgo,
            
            # Variable objetivo
            'aprobado': aprobado,
            'motivos_rechazo': '; '.join(motivo_rechazo) if motivo_rechazo else ''
        }
        
        datos.append(registro)
    
    return pd.DataFrame(datos)

if __name__ == '__main__':
    import os
    import sys
    
    try:
        print("="*60)
        print("Generando datos dummy para entrenamiento...")
        print("="*60)
        
        # Generar datos
        print("\n⏳ Generando 10,000 registros...")
        df = generar_datos(10000)
        
        # Crear carpeta data si no existe
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        os.makedirs(data_dir, exist_ok=True)
        print(f"✓ Carpeta de datos verificada: {os.path.abspath(data_dir)}")
        
        # Guardar datos
        csv_path = os.path.join(data_dir, 'datos_prestamos.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
        
        print(f"\n✅ Generación completada exitosamente!")
        print(f"   Total de registros: {len(df)}")
        print(f"   - Aprobados: {df['aprobado'].sum()} ({df['aprobado'].mean()*100:.1f}%)")
        print(f"   - Rechazados: {(1-df['aprobado']).sum()} ({(1-df['aprobado'].mean())*100:.1f}%)")
        print(f"\n📁 Archivo guardado: {os.path.abspath(csv_path)}")
        
    except Exception as e:
        print(f"\n❌ ERROR durante la generación de datos:")
        print(f"   {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    # Mostrar estadísticas detalladas
    print("\n📊 Estadísticas del dataset:")
    print(f"   Monto promedio solicitado: ${df['monto_solicitado'].mean():,.0f}")
    print(f"   Ingreso promedio: ${df['ingreso_principal'].mean():,.0f}")
    print(f"   Edad promedio: {df['edad'].mean():.1f} años")
    print(f"   Score de riesgo promedio: {df['score_riesgo'].mean():.1f}")
    
    # Análisis de rechazos
    rechazados = df[df['aprobado'] == 0]
    if len(rechazados) > 0:
        print(f"\n📉 Análisis de Rechazos ({len(rechazados)} casos):")
        
        # Contar motivos de rechazo
        motivos_contador = {}
        for motivos in rechazados['motivos_rechazo']:
            if motivos:
                for motivo in motivos.split('; '):
                    motivos_contador[motivo] = motivos_contador.get(motivo, 0) + 1
        
        print("   Principales motivos de rechazo:")
        for motivo, count in sorted(motivos_contador.items(), key=lambda x: x[1], reverse=True):
            porcentaje = (count / len(rechazados)) * 100
            print(f"   • {motivo}: {count} casos ({porcentaje:.1f}%)")
    
    # Estadísticas por aprobación
    print(f"\n💰 Análisis Financiero:")
    print(f"   Aprobados:")
    print(f"   - Ratio endeudamiento promedio: {df[df['aprobado']==1]['ratio_endeudamiento'].mean()*100:.1f}%")
    print(f"   - Capacidad de pago promedio: ${df[df['aprobado']==1]['capacidad_pago'].mean():,.0f}")
    print(f"   - Score de riesgo promedio: {df[df['aprobado']==1]['score_riesgo'].mean():.1f}")
    print(f"   Rechazados:")
    print(f"   - Ratio endeudamiento promedio: {df[df['aprobado']==0]['ratio_endeudamiento'].mean()*100:.1f}%")
    print(f"   - Capacidad de pago promedio: ${df[df['aprobado']==0]['capacidad_pago'].mean():,.0f}")
    print(f"   - Score de riesgo promedio: {df[df['aprobado']==0]['score_riesgo'].mean():.1f}")
