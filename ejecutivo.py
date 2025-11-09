from tipo_asiento import TipoAsiento

class Ejecutivo(TipoAsiento):
    def __init__(self):
        super().__init__()
        self._acceso_sala_vip = True
    
    def calcularCosto(self) -> float:
        return 1000000.0  
    
    def __str__(self) -> str:
        return "Asiento Ejecutivo"
