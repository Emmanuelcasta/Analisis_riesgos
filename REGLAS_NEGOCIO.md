# Reglas de Negocio - Sistema de Análisis de Préstamos

## 📋 Criterios de Rechazo Automático (Hard Rules)

El sistema rechaza automáticamente solicitudes que cumplan **cualquiera** de los siguientes criterios:

### 1. **Gastos Excesivos** 🚫
- **Regla**: Gastos mensuales > 60% de los ingresos totales
- **Motivo**: Capacidad de pago insuficiente para asumir nuevas obligaciones
- **Ejemplo**: Ingresos $3,000,000, Gastos $1,900,000 → RECHAZADO

### 2. **Ratio de Endeudamiento Alto** 🚫
- **Regla**: Cuota estimada > 40% de los ingresos totales
- **Motivo**: Compromiso financiero excesivo
- **Ejemplo**: Ingresos $2,000,000, Cuota $850,000 (42.5%) → RECHAZADO

### 3. **Capacidad de Pago Insuficiente** 🚫
- **Regla**: Capacidad de pago < 1.5x la cuota estimada
- **Motivo**: No hay margen suficiente para imprevistos
- **Ejemplo**: Capacidad $400,000, Cuota $300,000 (1.33x) → RECHAZADO

### 4. **Capacidad de Pago Negativa** 🚫
- **Regla**: (Ingresos - Gastos) ≤ 0
- **Motivo**: No hay flujo de caja disponible
- **Ejemplo**: Ingresos $2,000,000, Gastos $2,100,000 → RECHAZADO

### 5. **Edad Fuera de Rango** 🚫
- **Regla**: Edad < 20 años o Edad > 65 años
- **Motivo**: Riesgo actuarial o restricciones legales
- **Ejemplo**: Solicitante de 18 años → RECHAZADO

### 6. **Ingresos Muy Bajos** 🚫
- **Regla**: Ingresos < Salario Mínimo o Monto > 10x Ingresos
- **Motivo**: Ingresos insuficientes para el monto solicitado
- **Ejemplo**: Ingresos $1,200,000, Solicita $15,000,000 (12.5x) → RECHAZADO

### 7. **Contrato Inestable Reciente** 🚫
- **Regla**: Contrato temporal/servicios con < 1 año de antigüedad
- **Motivo**: Falta de estabilidad laboral
- **Ejemplo**: Prestación de servicios, 6 meses → RECHAZADO

### 8. **Carga Familiar Excesiva** 🚫
- **Regla**: ≥ 4 personas a cargo con ingresos < 3x Salario Mínimo
- **Motivo**: Gastos familiares comprometidos
- **Ejemplo**: 5 personas a cargo, Ingresos $3,500,000 → RECHAZADO

---

## 📊 Sistema de Scoring (Casos que pasan Hard Rules)

Para solicitudes que **NO son rechazadas automáticamente**, se aplica un sistema de puntaje (0-100):

### Componentes del Score:

#### 1. **Ratio de Endeudamiento** (30 puntos)
| Ratio | Puntos | Descripción |
|-------|--------|-------------|
| ≤ 20% | 30 | Endeudamiento muy bajo |
| 21-25% | 25 | Endeudamiento bajo |
| 26-30% | 20 | Endeudamiento moderado |
| 31-35% | 10 | Endeudamiento moderado-alto |
| 36-40% | 5 | Endeudamiento alto |

#### 2. **Capacidad de Pago vs Cuota** (25 puntos)
| Ratio | Puntos | Descripción |
|-------|--------|-------------|
| ≥ 3.0x | 25 | Capacidad excelente |
| 2.5-3.0x | 20 | Capacidad muy buena |
| 2.0-2.5x | 15 | Capacidad buena |
| 1.5-2.0x | 10 | Capacidad aceptable |
| < 1.5x | 5 | Capacidad mínima |

#### 3. **Ratio Gastos/Ingresos** (20 puntos)
| Ratio | Puntos | Descripción |
|-------|--------|-------------|
| ≤ 40% | 20 | Gastos muy controlados |
| 41-50% | 15 | Gastos controlados |
| 51-55% | 10 | Gastos moderados |
| 56-60% | 5 | Gastos altos |

#### 4. **Estabilidad Laboral** (15 puntos)
| Tipo Contrato | Antigüedad | Puntos |
|---------------|------------|--------|
| Indefinido | ≥ 3 años | 15 |
| Indefinido | ≥ 1 año | 12 |
| Fijo | ≥ 2 años | 10 |
| Independiente | ≥ 5 años | 10 |
| Cualquier | ≥ 1 año | 5 |
| Otros | < 1 año | 2 |

#### 5. **Nivel de Ingresos** (10 puntos)
| Ingresos (múltiplos del SM*) | Puntos |
|-------------------------------|--------|
| ≥ 5x | 10 |
| 4-5x | 8 |
| 3-4x | 6 |
| 2-3x | 4 |
| < 2x | 2 |

*SM = Salario Mínimo ($1,300,000)

### Bonificaciones Adicionales:
- **+3 puntos**: Otros ingresos ≥ 20% del ingreso principal
- **+2 puntos**: Propietario de vivienda
- **+2 puntos**: Nivel educativo profesional/posgrado
- **+3 puntos**: Edad óptima (28-55 años)

### Penalizaciones:
- **-3 puntos**: ≥ 3 personas a cargo
- **-5 puntos**: Contrato temporal o prestación de servicios

---

## ✅ Decisión Final

| Score | Decisión | Descripción |
|-------|----------|-------------|
| ≥ 70 | **APROBADO** | Perfil excelente, bajo riesgo |
| 60-69 | **Zona Gris** | Evaluación caso a caso (50% probabilidad) |
| < 60 | **RECHAZADO** | Perfil de alto riesgo |

---

## 📈 Estadísticas del Dataset

### Distribución de Aprobaciones:
- **Aprobados**: 31.2% (3,124 casos)
- **Rechazados**: 68.8% (6,876 casos)

### Principales Motivos de Rechazo:
1. **Ingresos insuficientes**: 49.7%
2. **Gastos exceden 60%**: 42.0%
3. **Muchas personas a cargo**: 40.7%
4. **Capacidad de pago insuficiente**: 37.9%
5. **Ratio endeudamiento alto**: 18.5%

### Análisis Financiero Comparativo:

| Métrica | Aprobados | Rechazados |
|---------|-----------|------------|
| **Ratio Endeudamiento** | 10.8% | 26.3% |
| **Capacidad de Pago** | $2,782,708 | $1,332,671 |
| **Score de Riesgo** | 85.0 | 42.5 |

---

## 🎯 Métricas del Modelo de IA

- **Accuracy**: 90.65%
- **Precision**: 82.02% (de los aprobados, 82% realmente deberían aprobarse)
- **Recall**: 89.76% (detecta correctamente 90% de buenos candidatos)
- **AUC-ROC**: 96.38% (excelente capacidad de discriminación)

### Matriz de Confusión:
- **Verdaderos Negativos**: 1,252 (rechazos correctos)
- **Verdaderos Positivos**: 561 (aprobaciones correctas)
- **Falsos Positivos**: 123 (aprobó incorrectamente)
- **Falsos Negativos**: 64 (rechazó incorrectamente)

---

## 💡 Ejemplos de Aplicación

### Ejemplo 1: APROBADO ✅
```
Edad: 35 años
Ingresos: $5,000,000
Gastos: $2,000,000 (40%)
Capacidad de pago: $3,000,000
Monto solicitado: $15,000,000
Cuota estimada: $375,000
Ratio endeudamiento: 7.5%
Ratio capacidad/cuota: 8.0x

Score: 88 puntos → APROBADO
```

### Ejemplo 2: RECHAZADO ❌
```
Edad: 28 años
Ingresos: $1,800,000
Gastos: $1,500,000 (83.3%)  ← Excede 60%
Capacidad de pago: $300,000
Monto solicitado: $10,000,000
Cuota estimada: $250,000

Motivo: Gastos exceden 60% de ingresos → RECHAZADO
```

### Ejemplo 3: ZONA GRIS ⚠️
```
Edad: 42 años
Ingresos: $3,000,000
Gastos: $1,700,000 (56.7%)
Capacidad de pago: $1,300,000
Monto solicitado: $10,000,000
Cuota estimada: $250,000
Ratio endeudamiento: 8.3%
Ratio capacidad/cuota: 5.2x

Score: 65 puntos → Evaluación manual requerida
```

---

## 🔄 Actualización del Modelo

Para mantener el modelo actualizado:

1. **Regenerar datos**:
   ```bash
   venv\Scripts\python.exe scripts\generar_datos_dummy.py
   ```

2. **Reentrenar modelo**:
   ```bash
   venv\Scripts\python.exe scripts\entrenar_modelo.py
   ```

3. **Sistema completo**:
   ```bash
   .\iniciar_sistema.bat
   ```

---

**Última actualización**: Noviembre 8, 2025
**Versión del modelo**: 2.0 (Reglas de negocio estrictas)
