from typing import List
from datetime import datetime
from avion import Avion

class Aerolinea:
    def __init__(self, nombre: str, codigo: str, paisOrigen: str, telefono: str, email: str):
        self.nombre = nombre
        self.codigo = codigo
        self.paisOrigen = paisOrigen
        self.telefono = telefono
        self.email = email
        self.aviones = []

    def agregarAvion(self, avion:Avion) ->None:
        if avion not in self.aviones:
            self.aviones.append(avion)
            avion.setAerolinea(self)

    def eliminarAvion(self,avion:Avion)->None:
        if avion in self.aviones:
            self.aviones.remove(avion)
            avion.setAerolinea(None)

    def buscarVuelos(self,criterio: str):
        print(f"Buscando vuelos con el criterio:{criterio}")
        return[]

    def getAviones(self):
        return self.aviones
    
    def __str__(self):
        return f"Aerolinea: {self.nombre} ({self.paisOrigen}) - {len(self.aviones)} aviones"