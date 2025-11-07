from avion import Avion
from estado_avion import EstadoAvion

def mostrar_menu():
    print("\n--- Sistema de Gestión de Aviones ---")
    print("1. Crear un nuevo avión")
    print("2. Ver información del avión")
    print("3. Ver todos los asientos")
    print("4. Reservar asiento")
    print("5. Cambiar estado del avión")
    print("6. Realizar mantenimiento")
    print("7. Actualizar horas de vuelo")
    print("8. Salir")

def main():
    avion = None
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            if avion is not None:
                print("¡Ya existe un avión creado!")
                continue
                
            matricula = input("Ingrese la matrícula del avión: ")
            modelo = input("Ingrese el modelo del avión: ")
            capacidad = int(input("Ingrese la capacidad total de pasajeros: "))
            
            avion = Avion(matricula, modelo, capacidad)
            print(f"\n¡Avión {modelo} creado exitosamente!")
            print(avion)
            
        elif opcion == "2":
            if avion is None:
                print("Primero debe crear un avión.")
                continue
                
            print("\n--- Información del Avión ---")
            print(avion)
            
        elif opcion == "3":
            if avion is None:
                print("Primero debe crear un avión.")
                continue
                
            print("\n--- Todos los Asientos ---")
            for asiento in avion.obtener_asientos():
                print(asiento)
                
        elif opcion == "4":
            if avion is None:
                print("Primero debe crear un avión.")
                continue
                
            try:
                num_asiento = input("Ingrese el número de asiento (ej: 1A, 2B): ")
                asiento = avion.obtener_asiento_por_numero(num_asiento)
                
                if not asiento.ocupado:
                    if asiento.reservarAsiento():
                        print(f"Asiento {num_asiento} reservado exitosamente.")
                        print(f"Costo: ${asiento.tipo.calcularCosto()}")
                else:
                    print(f"El asiento {num_asiento} ya está ocupado.")
                    
            except ValueError as e:
                print(f"Error: {str(e)}")
                
        elif opcion == "5":
            if avion is None:
                print("Primero debe crear un avión.")
                continue
                
            print("\nEstados disponibles:")
            print("1. OPERATIVO")
            print("2. MANTENIMIENTO")
            print("3. EN VUELO")
            
            opcion_estado = input("Seleccione el nuevo estado (1-3): ")
            
            if opcion_estado == "1":
                avion.cambiarEstado(EstadoAvion("OP001", "OPERATIVO"))
                print("Estado actualizado a OPERATIVO")
            elif opcion_estado == "2":
                avion.cambiarEstado(EstadoAvion("MT001", "MANTENIMIENTO"))
                print("Estado actualizado a MANTENIMIENTO")
            elif opcion_estado == "3":
                avion.cambiarEstado(EstadoAvion("VL001", "EN VUELO"))
                print("Estado actualizado a EN VUELO")
            else:
                print("Opción no válida")
                
        elif opcion == "6":
            if avion is None:
                print("Primero debe crear un avión.")
                continue
                
            avion.realizarMantenimiento()
            print("Avión puesto en mantenimiento.")
            print(avion.estado.obtenerEstadoActual())
            
        elif opcion == "7":
            if avion is None:
                print("Primero debe crear un avión.")
                continue
                
            try:
                horas = float(input("Ingrese las horas de vuelo a agregar: "))
                avion.horasVuelo += horas
                print(f"Horas de vuelo actualizadas: {avion.horasVuelo}")
            except ValueError:
                print("Error: Ingrese un número válido")
                
        elif opcion == "8":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Aviones")
    main()
