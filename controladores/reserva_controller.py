from flask import Blueprint, request, jsonify
from datetime import datetime
from Reserva import Reserva
from Pasajero import Pasajero
from EstadoReserva import EstadoReserva

# Lista para almacenar las reservas (simulando una base de datos)
reservas = []

# Crear un Blueprint para las rutas de reservas
reserva_bp = Blueprint('reserva', __name__)

# Obtener todas las reservas
@reserva_bp.route('/reservas', methods=['GET'])
def obtener_reservas():
    return jsonify([{
        'codigo': r.codigoReserva,
        'fecha': r.fechaReserva.isoformat(),
        'pasajero': r.pasajero,
        'vuelo': r.vuelo,
        'asiento': r.asiento,
        'precioTotal': r.precioTotal,
        'estado': str(r.estado)
    } for r in reservas])

# Obtener una reserva por código
@reserva_bp.route('/reservas/<string:codigo>', methods=['GET'])
def obtener_reserva(codigo):
    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    
    return jsonify({
        'codigo': reserva.codigoReserva,
        'fecha': reserva.fechaReserva.isoformat(),
        'pasajero': reserva.pasajero,
        'vuelo': reserva.vuelo,
        'asiento': reserva.asiento,
        'precioTotal': reserva.precioTotal,
        'estado': str(reserva.estado)
    })

# Crear una nueva reserva
@reserva_bp.route('/reservas', methods=['POST'])
def crear_reserva():
    datos = request.get_json()
    
    # Validar campos requeridos
    campos_requeridos = ['codigo', 'fecha', 'id_pasajero', 'vuelo', 'asiento', 'precio']
    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({'error': f'Falta el campo requerido: {campo}'}), 400
    
    # Verificar si el código de reserva ya existe
    if any(r.codigoReserva == datos['codigo'] for r in reservas):
        return jsonify({'error': 'Ya existe una reserva con este código'}), 409
    
    # Buscar al pasajero (en una aplicación real, esto buscaría en la base de datos)
    from ..controladores.pasajero_controller import pasajeros
    pasajero = next((p for p in pasajeros if p._Pasajero__identificacion == datos['id_pasajero']), None)
    
    if pasajero is None:
        return jsonify({'error': 'Pasajero no encontrado'}), 404
    
    # Crear la nueva reserva
    try:
        fecha_reserva = datetime.fromisoformat(datos['fecha'])
    except ValueError:
        return jsonify({'error': 'Formato de fecha inválido. Use el formato ISO (YYYY-MM-DDTHH:MM:SS)'}), 400
    
    nueva_reserva = Reserva(
        codigoReserva=datos['codigo'],
        fechaReserva=fecha_reserva,
        pasajero=datos['id_pasajero'],
        vuelo=datos['vuelo'],
        asiento=datos['asiento'],
        precioTotal=float(datos['precio'])
    )
    
    # Asociar la reserva al pasajero
    pasajero.agregarReserva(nueva_reserva)
    reservas.append(nueva_reserva)
    
    return jsonify({
        'mensaje': 'Reserva creada exitosamente',
        'codigo': datos['codigo']
    }), 201

# Actualizar estado de una reserva
@reserva_bp.route('/reservas/<string:codigo>/estado', methods=['PUT'])
def actualizar_estado_reserva(codigo):
    datos = request.get_json()
    
    if 'accion' not in datos:
        return jsonify({'error': 'Se requiere especificar una acción (confirmar o cancelar)'}), 400
    
    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    
    accion = datos['accion'].lower()
    
    if accion == 'confirmar':
        reserva.confirmarReserva()
        return jsonify({'mensaje': 'Reserva confirmada exitosamente'})
    elif accion == 'cancelar':
        reserva.cancelarReserva()
        return jsonify({'mensaje': 'Reserva cancelada exitosamente'})
    else:
        return jsonify({'error': 'Acción no válida. Use "confirmar" o "cancelar"'}), 400

# Asignar asiento a una reserva
@reserva_bp.route('/reservas/<string:codigo>/asiento', methods=['PUT'])
def asignar_asiento(codigo):
    datos = request.get_json()
    
    if 'asiento' not in datos:
        return jsonify({'error': 'Se debe especificar el número de asiento'}), 400
    
    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    
    if reserva.asignarAsiento(datos['asiento']):
        return jsonify({'mensaje': f'Asiento {datos["asiento"]} asignado exitosamente'})
    else:
        return jsonify({'error': 'No se pudo asignar el asiento'}), 400

# Generar boleto de una reserva
@reserva_bp.route('/reservas/<string:codigo>/boleto', methods=['GET'])
def generar_boleto(codigo):
    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    
    boleto = reserva.generarBoleto()
    return jsonify({'boleto': boleto})
