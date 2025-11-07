from abc import ABC, abstractmethod

class TipoAsiento(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def calcularCosto(self) -> float:
        pass
