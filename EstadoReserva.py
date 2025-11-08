from typing import List
from datetime import datetime

class EstadoReserva:
    def __init__(self, codigo: str, descripcion: str, esActivo: bool, permiteModificacion: bool, permiteCancelacion: bool, requiereConfirmacion: bool, usuarioCreacion: str):
        self.codigo = codigo 
        self.descripcion = descripcion
        self.esActivo = esActivo
        self.permiteModificacion = permiteModificacion
        self.permiteCancelacion = permiteCancelacion
        self.requiereConfirmacion = requiereConfirmacion
        self.fechaCreacion = datetime.now()
        self.usuarioCreacion = usuarioCreacion

    def get_estado(cls, codigo: str) -> 'EstadoReserva':
        
        if codigo == "PEND":
            return EstadoReserva(
                codigo="PEND", descripcion="Pendiente de Pago", esActivo=True, 
                permiteModificacion=True, permiteCancelacion=True, 
                requiereConfirmacion=False, usuarioCreacion="SYSTEM"
            )
        elif codigo == "CONF":
            return EstadoReserva(
                codigo="CONF", descripcion="Confirmada/Emitida", esActivo=True, 
                permiteModificacion=False, permiteCancelacion=True, 
                requiereConfirmacion=False, usuarioCreacion="SYSTEM"
            )
        elif codigo == "CANC":
            return EstadoReserva(
                codigo="CANC", descripcion="Cancelada", esActivo=False, 
                permiteModificacion=False, permiteCancelacion=False, 
                requiereConfirmacion=False, usuarioCreacion="SYSTEM"
            )
        else:
            raise ValueError(f"Código de estado '{codigo}' no válido")


    def puedeModificar(self) -> bool:
        return self.permiteModificacion

    def puedeCancelar(self) -> bool:
        return self.permiteCancelacion

    def requiereAccionUsuario(self) -> bool:
        return self.requiereConfirmacion

    def getEstadosValidos() -> List:
        return [
            EstadoReserva.get_estado("Pendiente"),
            EstadoReserva.get_estado("Confirmada"),
            EstadoReserva.get_estado("Cancelada")
        ]

    def __str__(self):
        
        return (f"Estado {self.codigo} ({self.descripcion})"
                f"Activo: {self.esActivo}, Modificable: {self.permiteModificacion}, "
                f"Cancelable: {self.permiteCancelacion}")
