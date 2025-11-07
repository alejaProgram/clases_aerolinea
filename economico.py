from tipo_asiento import TipoAsiento

class Economico(TipoAsiento):
    def __init__(self):
        super().__init__()
        self._espacio_extra = False
    
    def calcularCosto(self) -> float:
        return 100.0  
    
    def __str__(self) -> str:
        return "Asiento Económico"
