# ⚡ GUÍA VISUAL RÁPIDA

## 🎯 ¿Qué Hacer Ahora?

```
┌─────────────────────────────────────────────────────────┐
│  📦 PRIMERA VEZ - Instalación Completa                  │
└─────────────────────────────────────────────────────────┘

1️⃣  Abrir PowerShell o CMD
2️⃣  Navegar al proyecto:
    cd "C:\Users\melca\Documents\Universidad 2025-2\loan-ai-system"

3️⃣  Ejecutar:
    .\iniciar_sistema.bat

    ⏱️  Esto tomará ~10 minutos y hará:
    ✓ Generar 10,000 datos de entrenamiento
    ✓ Entrenar el modelo de IA
    ✓ Probar el modelo
    ✓ Iniciar la aplicación web

4️⃣  Abrir navegador en:
    http://localhost:5000

5️⃣  ¡A evaluar préstamos! 🎉
```

```
┌─────────────────────────────────────────────────────────┐
│  🚀 USO DIARIO - Ya está todo instalado                 │
└─────────────────────────────────────────────────────────┘

1️⃣  Abrir PowerShell o CMD
2️⃣  cd "C:\Users\melca\Documents\Universidad 2025-2\loan-ai-system"
3️⃣  .\iniciar_web.bat
4️⃣  Abrir http://localhost:5000
```

## 📸 Vista Previa del Flujo

```
┌───────────────────────┐
│   Abrir Navegador     │
│  localhost:5000       │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  📝 Formulario de     │
│    Solicitud          │
│                       │
│  Paso 1: Datos Gen.   │
│  Paso 2: Info Lab.    │
│  Paso 3: Finanzas     │
│                       │
│  [Analizar Solicitud] │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  🤖 IA Analiza        │
│                       │
│  Procesando datos...  │
│  Predicción...        │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  📊 Resultados        │
│                       │
│  ✅ APROBADO 75%      │
│  o                    │
│  ❌ RECHAZADO 35%     │
│                       │
│  + Métricas           │
│  + Gráficos           │
│  + Recomendaciones    │
└───────────────────────┘
```

## 🎮 Comandos Rápidos

```bash
# Primera vez (TODO)
iniciar_sistema.bat

# Solo web (ya entrenado)
iniciar_web.bat

# Solo instalar dependencias
instalar_dependencias.bat

# Pasos individuales
python scripts\generar_datos_dummy.py
python scripts\entrenar_modelo.py
python scripts\probar_modelo.py
python run.py
```

## 📊 Formulario Web - Campos Principales

```
┌─────────────────────────────────────────┐
│ 👤 PASO 1: Datos Generales              │
├─────────────────────────────────────────┤
│ • Tipo de documento                     │
│ • Número de documento                   │
│ • Nombres y apellidos                   │
│ • Celular y email                       │
│ • Fecha de nacimiento                   │
│ • Dirección y ciudad                    │
│ • Años en domicilio actual              │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ 💼 PASO 2: Información Laboral          │
├─────────────────────────────────────────┤
│ • Estado civil                          │
│ • Personas a cargo                      │
│ • Nivel de estudios                     │
│ • Ocupación                             │
│ • Tipo de contrato                      │
│ • Sector económico                      │
│ • Años de experiencia                   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ 💰 PASO 3: Información Financiera       │
├─────────────────────────────────────────┤
│ • Ingreso principal mensual             │
│ • Otros ingresos                        │
│ • Gastos mensuales                      │
│ • Monto del préstamo solicitado         │
│ • Plazo en meses                        │
│ • Línea de crédito                      │
└─────────────────────────────────────────┘
```

## 🎯 Ejemplo de Datos de Prueba

```
Copiar y pegar estos datos para probar:

Documento: 1234567890
Primer nombre: Juan
Apellido: Pérez
Celular: 3001234567
Email: juan.perez@email.com
Fecha nacimiento: 1985-05-15
Dirección: Calle 123 #45-67
Ciudad: Bogotá

Estado civil: Casado
Personas a cargo: 2
Estudios: Profesional
Ocupación: Empleado administrativo
Contrato: Indefinido
Experiencia: 10 años

Ingreso principal: $3,000,000
Gastos mensuales: $1,800,000
Monto solicitado: $10,000,000
Plazo: 24 meses
```

## 📈 Resultados que Verás

```
┌─────────────────────────────────────┐
│  PROBABILIDAD DE APROBACIÓN         │
│                                     │
│  ████████████████░░░░  75%          │
│                                     │
│  ✅ SOLICITUD APROBADA              │
│  Nivel de Riesgo: BAJO ⭐⭐⭐       │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  ANÁLISIS FINANCIERO                │
├─────────────────────────────────────┤
│  Ingresos Totales:    $3,000,000    │
│  Capacidad de Pago:   $1,200,000    │
│  Cuota Estimada:        $250,000    │
│  Ratio Endeudamiento:       8.3%    │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  GRÁFICO                            │
│  [Barras comparativas]              │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│  💡 RECOMENDACIONES                 │
│  ✓ Perfil cumple criterios          │
│  ✓ Capacidad de pago adecuada       │
└─────────────────────────────────────┘
```

## 🐛 ¿Problemas?

```
❌ Error: "Modelo no encontrado"
✅ Solución: python scripts\entrenar_modelo.py

❌ Error: "Puerto 5000 ocupado"
✅ Solución: Editar run.py cambiar puerto a 8080

❌ Error: "Module flask not found"
✅ Solución: instalar_dependencias.bat

❌ La web no carga
✅ Verificar: ¿El script sigue corriendo?
           ¿Hay errores en el terminal?
```

## 📚 ¿Más Info?

```
README.md          → Vista general y features
INICIO_RAPIDO.md   → Guía completa paso a paso
INSTALACION.md     → Instalación detallada
ESTRUCTURA.md      → Estructura del proyecto
CAMBIOS.md         → Qué se cambió y por qué
```

## ⚡ Atajos de Teclado

```
Ctrl + C           → Detener servidor web
F5 (navegador)     → Recargar página
Ctrl + Shift + I   → Abrir DevTools (depurar)
```

## 🎉 ¡Todo Listo!

```
┌───────────────────────────────────────┐
│                                       │
│    Tu Sistema de Préstamos con IA    │
│         está listo para usar         │
│                                       │
│    Ejecuta: iniciar_sistema.bat      │
│    Accede: http://localhost:5000     │
│                                       │
│           🚀 ¡Éxito! 🚀              │
│                                       │
└───────────────────────────────────────┘
```

---

**Tip:** Guarda este archivo como referencia rápida 💡
