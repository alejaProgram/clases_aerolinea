from flask import Blueprint, request, jsonify
from datetime import datetime, timezone
from Reserva import Reserva
from EstadoReserva import EstadoReserva

reservas = []

reserva_bp = Blueprint('reserva', __name__)

@reserva_bp.route('/reservas', methods=['GET'])
def obtener_reservas():
    return jsonify([{
        'codigo': r.codigoReserva,
        'fecha': r.fechaReserva.strftime('%d/%m/%Y'),
        'fecha_iso': r.fechaReserva.isoformat(),
        'pasajero': r.pasajero,
        'vuelo': r.vuelo,
        'asiento': r.asiento,
        'precioTotal': r.precioTotal,
        'estado': str(r.estado)
    } for r in reservas])

@reserva_bp.route('/reservas/<string:codigo>', methods=['GET'])
def obtener_reserva(codigo):
    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    
    return jsonify({
        'codigo': reserva.codigoReserva,
        'fecha': reserva.fechaReserva.strftime('%d/%m/%Y'),
        'fecha_iso': reserva.fechaReserva.isoformat(),
        'pasajero': reserva.pasajero,
        'vuelo': reserva.vuelo,
        'asiento': reserva.asiento,
        'precioTotal': reserva.precioTotal,
        'estado': reserva.estado.codigo
    })

@reserva_bp.route('/reservas', methods=['POST'])
def crear_reserva():
    datos = request.get_json()
    

    campos_requeridos = ['codigo', 'fecha', 'id_pasajero', 'vuelo', 'asiento', 'precio']
    for campo in campos_requeridos:
        if campo not in datos:
            return jsonify({'error': f'Falta el campo requerido: {campo}'}), 400
    

    if any(r.codigoReserva == datos['codigo'] for r in reservas):
        return jsonify({'error': 'Ya existe una reserva con este código'}), 409
    

    if not isinstance(datos['id_pasajero'], str) or not datos['id_pasajero'].strip():
        return jsonify({'error': 'ID de pasajero inválido'}), 400
    

    try:
        fecha_reserva = datetime.fromisoformat(datos['fecha'].replace('Z', '+00:00'))
        if fecha_reserva < datetime.now(timezone.utc):
            return jsonify({'error': 'La fecha de reserva no puede ser en el pasado'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Formato de fecha inválido. Use el formato ISO (YYYY-MM-DDTHH:MM:SS)'}), 400
    

    try:
        precio = float(datos['precio'])
        if precio <= 0:
            return jsonify({'error': 'El precio debe ser mayor a cero'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'Precio inválido'}), 400
    
    nueva_reserva = Reserva(
        codigoReserva=datos['codigo'],
        fechaReserva=fecha_reserva,
        pasajero=datos['id_pasajero'],
        vuelo=datos['vuelo'],
        asiento=datos['asiento'],
        precioTotal=float(datos['precio'])
    )
    

    if any(r.vuelo == datos['vuelo'] and r.asiento == datos['asiento'] 
           for r in reservas if r.estado != EstadoReserva.get_estado("CANC")):
        return jsonify({'error': 'El asiento ya está ocupado en este vuelo'}), 409
    

    reservas.append(nueva_reserva)
    
    return jsonify({
        'mensaje': 'Reserva creada exitosamente',
        'codigo': datos['codigo']
    }), 201


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
        return jsonify({
            'mensaje': 'Reserva confirmada exitosamente',
            'estado': reserva.estado.codigo
        })
    elif accion == 'cancelar':
        reserva.cancelarReserva()
        return jsonify({
            'mensaje': 'Reserva cancelada exitosamente',
            'estado': reserva.estado.codigo
        })
    else:
        return jsonify({'error': 'Acción no válida. Use "confirmar" o "cancelar"'}), 400


@reserva_bp.route('/reservas/<string:codigo>/asiento', methods=['PUT'])
def asignar_asiento(codigo):
    datos = request.get_json()
    

    if not datos or 'asiento' not in datos:
        return jsonify({'error': 'Se debe especificar el número de asiento'}), 400
    
    if not isinstance(datos['asiento'], str) or not datos['asiento'].strip():
        return jsonify({'error': 'El número de asiento no es válido'}), 400
    

    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    

    if any(r.vuelo == reserva.vuelo and r.asiento == datos['asiento'] and r != reserva 
           for r in reservas if r.estado != EstadoReserva.get_estado("CANC")):
        return jsonify({'error': 'El asiento ya está ocupado en este vuelo'}), 409
    

    if hasattr(reserva, 'asignarAsiento') and callable(getattr(reserva, 'asignarAsiento')):
        if reserva.asignarAsiento(datos['asiento']):
            return jsonify({
                'mensaje': f'Asiento {datos["asiento"]} asignado exitosamente',
                'asiento': datos['asiento']
            })
    
    return jsonify({'error': 'No se pudo asignar el asiento. Verifique el estado de la reserva.'}), 400


@reserva_bp.route('/reservas/<string:codigo>/boleto', methods=['GET'])
def generar_boleto(codigo):
    reserva = next((r for r in reservas if r.codigoReserva == codigo), None)
    if reserva is None:
        return jsonify({'error': 'Reserva no encontrada'}), 404
    

    if reserva.estado != EstadoReserva.get_estado("CONF"):
        return jsonify({'error': 'No se puede generar boleto para una reserva no confirmada'}), 400
    

    if not hasattr(reserva, 'generarBoleto') or not callable(getattr(reserva, 'generarBoleto')):
        return jsonify({
            'error': 'No se puede generar el boleto',
            'detalle': 'La funcionalidad de generación de boletos no está disponible'
        }), 501
    
    try: 
        boleto = reserva.generarBoleto()
        if not boleto:
            return jsonify({'error': 'No se pudo generar el boleto'}), 500
            
        return jsonify({
            'mensaje': 'Boleto generado exitosamente',
            'boleto': boleto,
            'reserva': {
                'codigo': reserva.codigoReserva,
                'fecha': reserva.fechaReserva.strftime('%d/%m/%Y'),
                'fecha_iso': reserva.fechaReserva.isoformat(),
                'vuelo': reserva.vuelo,
                'asiento': reserva.asiento,
                'precioTotal': reserva.precioTotal
            }
        })
    except Exception as e:
        return jsonify({
            'error': 'Error al generar el boleto',
            'detalle': str(e)
        }), 500
