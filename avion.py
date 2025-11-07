from typing import List
from asiento import Asiento
from estado_avion import EstadoAvion
from economico import Economico
from ejecutivo import Ejecutivo
from primera_clase import PrimeraClase

class Avion:
    def __init__(self, matricula: str, modelo: str, capacidad_total: int):
        self._matricula = matricula
        self._modelo = modelo
        self._capacidadTotal = capacidad_total
        self._horasVuelo = 0.0
        self._estado = EstadoAvion("OP001", "OPERATIVO")
        self._asientos: List[Asiento] = []
        self._aerolinea = None  
        
        self._inicializar_asientos()
    
    def _inicializar_asientos(self) -> None:
        total_asientos = self._capacidadTotal
        num_primera_clase = int(total_asientos * 0.3)
        num_ejecutivos = int(total_asientos * 0.2)
        
        fila = 1
        columna = 1
        max_columnas = 6  
        
        for i in range(num_primera_clase):
            numero = f"{fila}{chr(65 + columna - 1)}" 
            self._asientos.append(Asiento(numero, fila, columna, PrimeraClase()))
            columna += 1
            if columna > max_columnas:
                columna = 1
                fila += 1
        
        for i in range(num_ejecutivos):
            numero = f"{fila}{chr(65 + columna - 1)}"
            self._asientos.append(Asiento(numero, fila, columna, Ejecutivo()))
            columna += 1
            if columna > max_columnas:
                columna = 1
                fila += 1
        
        num_economicos = total_asientos - num_primera_clase - num_ejecutivos
        for i in range(num_economicos):
            numero = f"{fila}{chr(65 + columna - 1)}"
            self._asientos.append(Asiento(numero, fila, columna, Economico()))
            columna += 1
            if columna > max_columnas:
                columna = 1
                fila += 1
    
    @property
    def matricula(self) -> str:
        return self._matricula
    
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @property
    def capacidadTotal(self) -> int:
        return self._capacidadTotal
    
    @property
    def horasVuelo(self) -> float:
        return self._horasVuelo
    
    @horasVuelo.setter
    def horasVuelo(self, horas: float) -> None:
        self._horasVuelo = horas
    
    @property
    def estado(self) -> EstadoAvion:
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado: EstadoAvion) -> None:
        self._estado = nuevo_estado
    
    @property
    def aerolinea(self):
        return self._aerolinea
    
    @aerolinea.setter
    def aerolinea(self, aerolinea) -> None:
        self._aerolinea = aerolinea
    
    def asignarVuelo(self, vuelo) -> bool:
        return True
    
    def realizarMantenimiento(self) -> None:
        self._estado = EstadoAvion("MT001", "MANTENIMIENTO")
        self._estado.cambiarEstado()
    
    def cambiarEstado(self, nuevo_estado: EstadoAvion) -> None:
        self._estado = nuevo_estado
        self._estado.cambiarEstado()
    
    def obtenerAsientosDisponibles(self) -> int:
        return sum(1 for asiento in self._asientos if not asiento.ocupado)
    
    def setAerolinea(self, aerolinea) -> None:
        self._aerolinea = aerolinea
    
    def getAerolinea(self):
        return self._aerolinea
    
    def obtener_asientos(self) -> List[Asiento]:
        return self._asientos.copy()
    
    def obtener_asiento_por_numero(self, numero: str) -> Asiento:
        for asiento in self._asientos:
            if asiento.numero == numero:
                return asiento
        raise ValueError(f"No existe el asiento número {numero}")
    
    def __str__(self) -> str:
        return (f"Avión {self._modelo} (Matrícula: {self._matricula})\n"
                f"Capacidad: {self._capacidadTotal} pasajeros\n"
                f"Horas de vuelo: {self._horasVuelo}\n"
                f"Estado: {self._estado.descripcion}\n"
                f"Asientos disponibles: {self.obtenerAsientosDisponibles()} de {self._capacidadTotal}")
