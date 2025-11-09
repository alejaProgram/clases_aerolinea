from Aeropuerto import Aeropuerto   
from EstadoVuelo import EstadoVuelo
from Aerolinea import Aerolinea
from datetime import datetime

class Vuelo:
    def __init__(self,numeroVuelo: str, aeropuertoOrigen: Aeropuerto, aeropuertoDestino: Aeropuerto, fechaSalida: datetime, fechaLlegada: datetime, avion:str,precio: float, aerolinea: Aerolinea, estado: EstadoVuelo = None):
        self.numeroVuelo = numeroVuelo
        self.aeropuertoOrigen = aeropuertoOrigen
        self.aeropuertoDestino = aeropuertoDestino
        self.fechaSalida = fechaSalida
        self.fechaLlegada = fechaLlegada
        self.avion = avion
        self.precio = precio
        self.aerolinea = aerolinea

        if estado is None:
            self.estado = EstadoVuelo("PROG", "Programado")
        else:
            self.estado = estado

    def asignarAvion(self, avion: str):
        self.avion = avion
        print(f"Avion {avion} asignado al vuelo {self.numeroVuelo}")

    def calcularDuracion(self):
        return self.fechaLlegada - self.fechaSalida

    def cambiarEstado(self, nuevoEstado: EstadoVuelo):
        self.estado = nuevoEstado  
        print(f"Estado del vuelo {self.numeroVuelo} cambiado a: {self.estado.descripcion}")

    def obtenerPrecio(self):   
        return self.precio
    
    def getAsientoDisponibles(self):
        return 50

    def consultarDisponibilidad(self):
        asientos = self.getAsientoDisponibles()
        if asientos > 0:
            print(f"Hay {asientos} asientos disponibles en el vuelo {self.numeroVuelo}")
        else:
            print(f"El vuelo {self.numeroVuelo} no tiene asientos disponibles")            
   
    def __str__(self):
        return (f"Vuelo #: {self.numeroVuelo}\n"
                f" Origen: {self.aeropuertoOrigen.codigo}, Destino: {self.aeropuertoDestino.codigo}"
                f"Salida: {self.fechaSalida}, Llegada: {self.fechaLlegada}"
                f"Avion: {self.avion}, Precio: {self.precio}"
                f"Estado: {self.estado.descripcion}")

