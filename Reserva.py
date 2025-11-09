from EstadoReserva import EstadoReserva
from typing import List
from typing import Optional
from datetime import datetime

class Reserva:
    def __init__(self, codigoReserva: str, fechaReserva: datetime, pasajero: str, vuelo: str, asiento: str, precioTotal: float, estado: Optional[EstadoReserva]= None):
        self.codigoReserva = codigoReserva                 
        self.fechaReserva = fechaReserva         
        self.pasajero = pasajero                             
        self.vuelo = vuelo                                   
        self.asiento = asiento                                     
        self.precioTotal = precioTotal                       

        if estado is None:
            self.estado = EstadoReserva.get_estado("PEND")
        else: 
            self.estado = estado
    
    def __str__(self):
        asiento_info = self.asiento if self.asiento else 'No Asignado'
        return (f"Reserva: {self.codigoReserva}, Estado:{self.estado.codigo}"
                f"Vuelo: {self.vuelo}"
                f"Pasajero: {self.pasajero}"
                f"Asiento: {asiento_info}, Precio Total: ${self.precioTotal:,.0f} COP")
   
    def asignarAsiento(self, asiento: str) -> bool:
        if self.estado.puedeModificar():
            self.asiento = asiento
            print(f"Asiento {asiento} asignado a {self.pasajero}")
            return True
        else:
            print(f"No se puede modificar el asiento actual")
            return False

    def confirmarReserva(self) -> None:
        if self.estado.requiereAccionUsuario():
            self.estado = EstadoReserva.get_estado("CONF")
            print(f"Reserva ha sido confirmada")
        else:
            print(f"Esta reserva no requiere confirmacion")

    def cancelarReserva(self) -> None:
        if self.estado.puedeCancelar():
            self.estado = EstadoReserva.get_estado("CANC")
            print(f"Reserva ha sido cancelada")
        else:
            print(f"No se puede cancelar la reserva actual")

    def calcularPrecioTotal(self) -> float:
        return self.precioTotal

    def generarBoleto(self) -> str:
        if self.estado != "Confirmada":
            return f"No se puede generar el boleto. Estado: {self.estado}"
            
        boleto = (
            f"--- BOLETO {self.codigoReserva} ---\n"
            f"Codigo de reserva: {self.codigoReserva}\n"
            f"Pasajero: {self.pasajero}\n"
            f"Vuelo: {self.vuelo}\n"
            f"Asiento: {self.asiento if self.asiento else 'Sin asignar'}\n"
            f"Precio Pagado: ${self.precioTotal:,.0f} COP\n"
            f"---------------------------------------"
        )
        return boleto

