from flask import Flask, jsonify
from controladores.pasajero_controller import pasajero_bp
from controladores.reserva_controller import reserva_bp
import os

def create_app():
    app = Flask(__name__)
    
    app.config['JSON_AS_ASCII'] = False  # Para soportar caracteres especiales
    app.config['JSON_SORT_KEYS'] = False  # Para mantener el orden de los campos en el JSON
    
    # Estos son los blueprints
    app.register_blueprint(pasajero_bp, url_prefix='/api')
    app.register_blueprint(reserva_bp, url_prefix='/api')
    
    # Esta es la bienvenida
    @app.route('/')
    def index():
        return jsonify({
            'mensaje': 'Bienvenido a la API de Gestión de Aerolínea',
            'endpoints': {
                'pasajeros': '/api/pasajeros',
                'reservas': '/api/reservas'
            }
        })
    
  
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Recurso no encontrado'}), 404
    

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Error interno del servidor'}), 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
