"""
Inicialización de la aplicación Flask
"""
from flask import Flask

def create_app():
    """Factory para crear la aplicación Flask"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
    
    # Registrar blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app
