from EstadoReserva import EstadoReserva
from typing import List
from typing import Optional
from datetime import datetime

class Asiento:
    def __init__(self, codigo: str):
        self.codigo = codigo

    def __str__(self):
        return f"Asiento {self.codigo}"

class Reserva:
    def __init__(self, codigoReserva: str, fechaReserva: datetime, pasajero: str, vuelo: str, asiento: str, precioTotal: float, estado: Optional[EstadoReserva]= None):
        self.codigoReserva = codigoReserva                 
        self.fechaReserva = fechaReserva         
        self.pasajero = pasajero                             
        self.vuelo = vuelo                                   
        self.asiento = asiento                                     
        self.precioTotal = precioTotal                       

        if estado is None:
            self.estado = EstadoReserva.PENDIENTE
        else: 
            self.estado = estado
    
    def __str__(self):
        asiento_info = self.asiento.codigo if self.asiento else 'No Asignado'
        return (f"Reserva: {self._codigo_reserva}, Estado:{self.estado.value}"
                f"Vuelo: {self.vuelo.numero} ({self.vuelo.destino})"
                f"Pasajero: {self.pasajero.nombre} {self.pasajero.apellido}"
                f"Asiento: {asiento_info}, Precio Total:{self.precioTotal:.2f}")
   
    def asignarAsiento(self, asiento: Asiento) -> bool:
        if self.estadoPuedeModificar():
            self.asiento = asiento
            print(f"Asiento {asiento} asignado a {self.pasajero.nombre}")
            return True
        else:
            print(f"No se puede modificar el asiento actual")
            return False

    def confirmarReserva(self) -> None:
        if self.estadoRequiereAccionUsuario():
            self.estado = EstadoReserva.CONFIRMADA
            print(f"Reserva ha sido confirmada")
        else:
            print(f"Esta reserva np requiere confirmacion")

    def cancelarReserva(self) -> None:
        if self.estadoPuedeCancelar():
            self.estado = EstadoReserva.CANCELADA
            print(f"Reserva ha sido cancelada")
        else:
            print(f"No se puede cancelar la reserva actual")

    def calcularPrecioTotal(self) -> float:
        return self.precioTotal()

    def generarBoleto(self) -> str:
        if self.estado != "Confirmada":
            return f"No se puede generar el boleto. Estado: {self.estado}"
            
        boleto = (
            f"--- BOLETO {self._codigo_reserva} ---"
            f"Codigo de reserva: {self.codidoReserva}"
            f"Pasajero: {self.pasajero.nombre} {self.pasajero.apellido}"
            f"Vuelo: {self.vuelo.numero} ({self.vuelo.origen} - {self.vuelo.destino})"
            f"Asiento: {self.asiento.codigo if self.asiento else 'Sin asignar'}"
            f"Precio Pagado:{self.precioTotal:.2f}"
            f"---------------------------------------"
        )
        return boleto

