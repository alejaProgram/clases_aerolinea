from tipo_asiento import TipoAsiento

class Asiento:
    def __init__(self, numero: str, fila: int, columna: int, tipo: TipoAsiento):
        self._numero = numero
        self._fila = fila
        self._columna = columna
        self._tipo = tipo
        self._ocupado = False
    
    @property
    def numero(self) -> str:
        return self._numero
    
    @property
    def fila(self) -> int:
        return self._fila
    
    @property
    def columna(self) -> int:
        return self._columna
    
    @property
    def tipo(self) -> TipoAsiento:
        return self._tipo
    
    @property
    def ocupado(self) -> bool:
        return self._ocupado
    
    def reservarAsiento(self) -> bool:
        if not self._ocupado:
            self._ocupado = True
            return True
        return False
    
    def __str__(self) -> str:
        tipo_nombre = self._tipo.__class__.__name__
        return f"Asiento {self._numero} (Fila {self._fila}, Col {self._columna}) - {tipo_nombre} - {'Ocupado' if self._ocupado else 'Disponible'}"
