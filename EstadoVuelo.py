class EstadoVuelo:
    def __init__(self, codigo: str, descripcion: str, activo: bool = True):
        self.codigo = codigo
        self.descripcion = descripcion
        self.activo = activo

    def cambiarEstado(self):
        self.activo = not self.activo
        print(f"Estado '{self.descripcion}' (Código: {self.codigo}) cambiado a activo={self.activo}")
    
    def __str__(self):
        return f"EstadoVuelo [Codigo: {self.codigo}, Descripción: {self.descripcion}, Activo: {self.activo}]"
    
