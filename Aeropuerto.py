class Aeropuerto:
    def __init__(self, codigo: str, nombre: str, ciudad: str, pais: str, zonaHoraria: str, latitud: float, longitud: float):
        self.codigo = codigo
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.zonaHoraria = zonaHoraria
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
        return (f"Aeropuerto: {self.nombre}({self.codigo})"
                f"Ubicacion: {self.ciudad}, {self.pais}"
                f"Coordenadas: Latitud {self.latitud}, Longitud {self.longitud}")
    
