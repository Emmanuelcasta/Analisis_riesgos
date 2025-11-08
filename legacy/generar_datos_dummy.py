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
        años_domicilio = np.random.randint(0, 30)
        
        # Nacimiento
        edad = np.random.randint(18, 75)
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
        personas_a_cargo = np.random.randint(0, 6)
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
        
        tiempo_desarrollo_actividad = np.random.randint(1, min(edad - 17, 30))
        tiempo_en_actividad = np.random.randint(1, tiempo_desarrollo_actividad + 1)
        nivel_estudios = random.choice(NIVELES_ESTUDIO)
        titulo_profesional = fake.job() if nivel_estudios in ['Profesional', 'Posgrado'] else ''
        
        # Ingresos y gastos (coherentes con ocupación y edad)
        if tipo_contrato == 'Independiente':
            ingreso_base = np.random.randint(800000, 5000000)
        elif nivel_estudios in ['Profesional', 'Posgrado']:
            ingreso_base = np.random.randint(2000000, 10000000)
        else:
            ingreso_base = np.random.randint(1300000, 4000000)
        
        ingreso_principal = int(ingreso_base * np.random.uniform(0.9, 1.1))
        fuente_ingresos = 'Salario' if tipo_contrato != 'Independiente' else 'Negocio propio'
        otros_ingresos = int(np.random.uniform(0, 1000000)) if random.random() > 0.6 else 0
        gastos_mensuales = int(ingreso_principal * np.random.uniform(0.4, 0.85))
        
        # CRITERIOS DE DECISIÓN - REGLAS DE NEGOCIO
        # Calculamos variables derivadas para el scoring
        capacidad_pago = ingreso_principal + otros_ingresos - gastos_mensuales
        cuota_estimada = monto_solicitado * 0.025  # Estimación simplificada
        ratio_endeudamiento = cuota_estimada / (ingreso_principal + otros_ingresos) if ingreso_principal > 0 else 1
        ratio_ahorro = capacidad_pago / (ingreso_principal + otros_ingresos) if ingreso_principal > 0 else 0
        
        # Factores de riesgo
        score_riesgo = 0
        
        # Factor 1: Capacidad de pago (40% del score)
        if ratio_endeudamiento <= 0.30:
            score_riesgo += 40
        elif ratio_endeudamiento <= 0.40:
            score_riesgo += 25
        elif ratio_endeudamiento <= 0.50:
            score_riesgo += 15
        else:
            score_riesgo += 0
        
        # Factor 2: Estabilidad laboral (25% del score)
        if años_empresa >= 3:
            score_riesgo += 25
        elif años_empresa >= 1:
            score_riesgo += 15
        elif años_empresa >= 0.5:
            score_riesgo += 8
        
        if tipo_contrato in ['Indefinido', 'Independiente']:
            score_riesgo += 5
        
        # Factor 3: Nivel de ingresos (15% del score)
        salario_minimo = 1300000
        if ingreso_principal >= 4 * salario_minimo:
            score_riesgo += 15
        elif ingreso_principal >= 2 * salario_minimo:
            score_riesgo += 10
        elif ingreso_principal >= salario_minimo:
            score_riesgo += 5
        
        # Factor 4: Perfil demográfico (10% del score)
        if 25 <= edad <= 60:
            score_riesgo += 8
        elif 18 <= edad < 25 or 60 < edad <= 70:
            score_riesgo += 4
        
        if nivel_estudios in ['Profesional', 'Posgrado', 'Tecnólogo']:
            score_riesgo += 5
        elif nivel_estudios == 'Técnico':
            score_riesgo += 3
        
        # Factor 5: Estabilidad residencial (5% del score)
        if es_arrendador or años_domicilio >= 3:
            score_riesgo += 5
        elif años_domicilio >= 1:
            score_riesgo += 3
        
        # Factor 6: Diversificación de ingresos (5% del score)
        if otros_ingresos > 0:
            score_riesgo += 5
        
        # Penalizaciones
        if personas_a_cargo >= 4:
            score_riesgo -= 5
        if gastos_mensuales / ingreso_principal > 0.8:
            score_riesgo -= 10
        
        # Decisión final: Aprobado si score >= 60
        aprobado = 1 if score_riesgo >= 60 else 0
        
        # Si capacidad de pago es negativa, rechazar automáticamente
        if capacidad_pago < cuota_estimada * 1.2:
            aprobado = 0
            score_riesgo = min(score_riesgo, 50)
        
        # Agregar algo de aleatoriedad realista (casos límite)
        if 55 <= score_riesgo <= 65:
            aprobado = 1 if random.random() > 0.3 else 0
        
        registro = {
            # Paso 1: Datos Generales
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
            
            # Paso 2: Conocimiento
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
            'aprobado': aprobado
        }
        
        datos.append(registro)
    
    return pd.DataFrame(datos)

if __name__ == '__main__':
    print("Generando datos dummy para entrenamiento...")
    df = generar_datos(10000)
    
    # Guardar datos
    df.to_csv('datos_prestamos.csv', index=False)
    print(f"\n✅ Generados {len(df)} registros")
    print(f"   - Aprobados: {df['aprobado'].sum()} ({df['aprobado'].mean()*100:.1f}%)")
    print(f"   - Rechazados: {(1-df['aprobado']).sum()} ({(1-df['aprobado'].mean())*100:.1f}%)")
    print(f"\nArchivo guardado: datos_prestamos.csv")
    
    # Mostrar estadísticas
    print("\n📊 Estadísticas del dataset:")
    print(f"   Monto promedio solicitado: ${df['monto_solicitado'].mean():,.0f}")
    print(f"   Ingreso promedio: ${df['ingreso_principal'].mean():,.0f}")
    print(f"   Edad promedio: {df['edad'].mean():.1f} años")
    print(f"   Score de riesgo promedio: {df['score_riesgo'].mean():.1f}")
