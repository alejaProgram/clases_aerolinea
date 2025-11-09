from datetime import datetime

class EstadoAvion:
    def __init__(self, codigo: str, descripcion: str):
        self._codigo = codigo
        self._descripcion = descripcion
        self._fechaHoraInicio = datetime.now()
        self._fechaPublicacion = datetime.now()
        self._ubicacionActual = ""
        self._cantidadCombustible = 0.0
        self._altitudActual = 0.0
    
    @property
    def codigo(self) -> str:
        return self._codigo
    
    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @property
    def fechaHoraInicio(self) -> datetime:
        return self._fechaHoraInicio
    
    @property
    def fechaPublicacion(self) -> datetime:
        return self._fechaPublicacion
    
    @property
    def ubicacionActual(self) -> str:
        return self._ubicacionActual
    
    @ubicacionActual.setter
    def ubicacionActual(self, valor: str) -> None:
        self._ubicacionActual = valor
    
    @property
    def cantidadCombustible(self) -> float:
        return self._cantidadCombustible
    
    @cantidadCombustible.setter
    def cantidadCombustible(self, valor: float) -> None:
        self._cantidadCombustible = valor
    
    @property
    def altitudActual(self) -> float:
        return self._altitudActual
    
    @altitudActual.setter
    def altitudActual(self, valor: float) -> None:
        self._altitudActual = valor
    
    def cambiarEstado(self) -> None:
        self._fechaHoraInicio = datetime.now()
    
    def obtenerEstadoActual(self) -> str:
        return (f"Estado: {self._descripcion}\n"
                f"Código: {self._codigo}\n"
                f"Ubicación: {self._ubicacionActual}\n"
                f"Combustible: {self._cantidadCombustible}\n"
                f"Altitud: {self._altitudActual}")
    
    def registrarUbicacion(self) -> None:
        self._fechaPublicacion = datetime.now()
    
    def mostrarInformacion(self) -> str:
        return self.obtenerEstadoActual()
