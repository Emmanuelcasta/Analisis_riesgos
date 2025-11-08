"""
Script principal para ejecutar la aplicación Flask
"""
from app import create_app

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
