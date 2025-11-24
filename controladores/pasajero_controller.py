from flask import Blueprint, request, jsonify
from ..Pasajero import Pasajero

# Lista para almacenar los pasajeros (simulando una base de datos)
pasajeros = []

# Crear un Blueprint para las rutas de pasajeros
pasajero_bp = Blueprint('pasajero', __name__)

# Obtener todos los pasajeros
@pasajero_bp.route('/pasajeros', methods=['GET'])
def obtener_pasajeros():
    return jsonify([{
        'identificacion': p._Pasajero__identificacion,
        'nombre': p.nombre,
        'apellido': p.apellido,
        'edad': p.edad,
        'nacionalidad': p.nacionalidad,
        'telefono': p.telefono,
        'email': p.email,
        'total_reservas': len(p.reservas)
    } for p in pasajeros])

# Obtener un pasajero por ID
@pasajero_bp.route('/pasajeros/<string:id>', methods=['GET'])
def obtener_pasajero(id):
    pasajero = next((p for p in pasajeros if p._Pasajero__identificacion == id), None)
    if pasajero is None:
        return jsonify({'error': 'Pasajero no encontrado'}), 404
    
    return jsonify({
        'identificacion': pasajero._Pasajero__identificacion,
        'nombre': pasajero.nombre,
        'apellido': pasajero.apellido,
        'edad': pasajero.edad,
        'nacionalidad': pasajero.nacionalidad,
        'telefono': pasajero.telefono,
        'email': pasajero.email,
        'reservas': [{
            'codigo': r.codigoReserva,
            'vuelo': r.vuelo,
            'estado': str(r.estado)
        } for r in pasajero.reservas]
    })

# Crear un nuevo pasajero
@pasajero_bp.route('/pasajeros', methods=['POST'])
def crear_pasajero():
    datos = request.get_json()
    
    # Validar que todos los campos requeridos estén presentes
    campos_requeridos = ['identificacion', 'nombre', 'apellido', 'edad', 'nacionalidad', 'telefono', 'email']
    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({'error': f'Falta el campo requerido: {campo}'}), 400
    
    # Verificar si el pasajero ya existe
    if any(p._Pasajero__identificacion == datos['identificacion'] for p in pasajeros):
        return jsonify({'error': 'Ya existe un pasajero con esta identificación'}), 409
    
    # Crear el nuevo pasajero
    nuevo_pasajero = Pasajero(
        identificacion=datos['identificacion'],
        nombre=datos['nombre'],
        apellido=datos['apellido'],
        edad=datos['edad'],
        nacionalidad=datos['nacionalidad'],
        telefono=datos['telefono'],
        email=datos['email']
    )
    
    pasajeros.append(nuevo_pasajero)
    return jsonify({'mensaje': 'Pasajero creado exitosamente', 'id': datos['identificacion']}), 201

# Actualizar información de un pasajero
@pasajero_bp.route('/pasajeros/<string:id>', methods=['PUT'])
def actualizar_pasajero(id):
    datos = request.get_json()
    pasajero = next((p for p in pasajeros if p._Pasajero__identificacion == id), None)
    
    if pasajero is None:
        return jsonify({'error': 'Pasajero no encontrado'}), 404
    
    # Actualizar solo los campos proporcionados
    if 'telefono' in datos:
        pasajero.telefono = datos['telefono']
    if 'email' in datos:
        pasajero.email = datos['email']
    
    return jsonify({'mensaje': 'Información del pasajero actualizada exitosamente'})

# Eliminar un pasajero
@pasajero_bp.route('/pasajeros/<string:id>', methods=['DELETE'])
def eliminar_pasajero(id):
    global pasajeros
    pasajeros = [p for p in pasajeros if p._Pasajero__identificacion != id]
    return jsonify({'mensaje': 'Pasajero eliminado exitosamente'})
