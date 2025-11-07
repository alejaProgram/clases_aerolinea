from tipo_asiento import TipoAsiento

class PrimeraClase(TipoAsiento):
    def __init__(self):
        super().__init__()
        self._servicio_premium = True
    
    def calcularCosto(self) -> float:
        return 500.0  
    
    def __str__(self) -> str:
        return "Asiento Primera Clase"
