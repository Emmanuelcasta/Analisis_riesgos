// Funciones JavaScript para el sistema de préstamos

// Formatear números como moneda colombiana
function formatCurrency(value) {
    return new Intl.NumberFormat('es-CO', {
        style: 'currency',
        currency: 'COP',
        minimumFractionDigits: 0
    }).format(value);
}

// Calcular y mostrar totales en tiempo real
document.addEventListener('DOMContentLoaded', function() {
    const ingresoPrincipalInput = document.querySelector('[name="ingreso_principal"]');
    const otrosIngresosInput = document.querySelector('[name="otros_ingresos"]');
    const gastosMensualesInput = document.querySelector('[name="gastos_mensuales"]');
    
    if (ingresoPrincipalInput && otrosIngresosInput && gastosMensualesInput) {
        const updateCalculations = () => {
            const ingresoPrincipal = parseFloat(ingresoPrincipalInput.value) || 0;
            const otrosIngresos = parseFloat(otrosIngresosInput.value) || 0;
            const gastosMensuales = parseFloat(gastosMensualesInput.value) || 0;
            
            const totalIngresos = ingresoPrincipal + otrosIngresos;
            const capacidadPago = totalIngresos - gastosMensuales;
            
            console.log('Total ingresos:', totalIngresos);
            console.log('Capacidad de pago:', capacidadPago);
        };
        
        ingresoPrincipalInput.addEventListener('input', updateCalculations);
        otrosIngresosInput.addEventListener('input', updateCalculations);
        gastosMensualesInput.addEventListener('input', updateCalculations);
    }
});

// Validación de formulario
const form = document.getElementById('loanForm');
if (form) {
    form.addEventListener('submit', function(e) {
        const ingresoPrincipal = parseFloat(document.querySelector('[name="ingreso_principal"]').value);
        const gastosMensuales = parseFloat(document.querySelector('[name="gastos_mensuales"]').value);
        const montoSolicitado = parseFloat(document.querySelector('[name="monto_solicitado"]').value);
        
        // Validar que los ingresos sean mayores a los gastos
        if (gastosMensuales >= ingresoPrincipal) {
            alert('⚠️ Los gastos mensuales deben ser menores que los ingresos principales');
            e.preventDefault();
            return false;
        }
        
        // Validar monto mínimo
        if (montoSolicitado < 500000) {
            alert('⚠️ El monto mínimo del préstamo es $500,000 COP');
            e.preventDefault();
            return false;
        }
        
        // Mostrar spinner de carga
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span> Analizando...';
        }
        
        return true;
    });
}

// Animación suave al cargar la página
window.addEventListener('load', function() {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.3s';
        document.body.style.opacity = '1';
    }, 100);
});
