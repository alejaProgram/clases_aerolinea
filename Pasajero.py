from Reserva import Reserva


class Pasajero:
    def __init__(self, identificacion: str, nombre: str, apellido: str, edad: int, nacionalidad: str, telefono: str, email: str):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.telefono = telefono
        self.email = email
        self.reservas = []
    
    def actualizarInformacion(self, telefono: str, email: str):
        self.telefono = telefono
        self.email = email
        print(f"Informacion actualizada correctamente")

    def calcularEdad(self):
        return self.edad

    def consultarReservas(self):
        if not self.reservas:
            print(f"El pasajero {self.nombre} no tiene reservas")
        else:
            for reserva in self.reservas:
                print(f"Codigo: {reserva.codigoReserva}, Vuelo: {reserva.vuelo}, Estado: {reserva.estado}")
    
    def cancelarReserva(self, codigo_reserva: str)-> bool:
        for reserva in self.reservas:
            if reserva.codigoReserva == codigo_reserva:
                reserva.cancelarReserva()
                print(f"Reserva {codigo_reserva} ha sido cancelada")
                return True
        print(f"Reserva no encontrada")
        return False
                
    def agregarReserva(self, reserva: Reserva):
        self.reservas.append(reserva)
        print(f"Reserva {reserva.codigoReserva} agregada")
            
    def __str__(self):
            return (f"Pasajero: {self.nombre} {self.apellido} (ID: {self.__identificacion})"
                    f"Edad:{self.edad} Nacionalidad: {self.nacionalidad}"
                    f"Telefono: {self.telefono} Email: {self.email}"
                    f" Total Reservas: {len(self.reservas)}")

