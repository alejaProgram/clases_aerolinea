from avion import Avion
from estado_avion import EstadoAvion
import time
import sys

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

def convertir_hora_12_a_24(hora_str):
    hora_str = hora_str.strip().upper()

    if 'AM' not in hora_str and 'PM' not in hora_str:
        return float(hora_str)
    
    if 'AM' in hora_str:
        es_pm = False
        hora_str = hora_str.replace('AM', '').strip()
    else:
        es_pm = True
        hora_str = hora_str.replace('PM', '').strip()
    
    if ':' in hora_str:
        partes = hora_str.split(':')
        horas = int(partes[0])
        minutos = int(partes[1])
    else:
        horas = int(hora_str)
        minutos = 0
    
    if es_pm and horas != 12:
        horas += 12
    elif not es_pm and horas == 12:
        horas = 0
    
    return horas + (minutos / 60.0)

def animacion_cierre():
    mensajes = [
        "\n✈️  Cerrando sistema",
        "✈️  Cerrando sistema.",
        "✈️  Cerrando sistema..",
        "✈️  Cerrando sistema...",
    ]
    
    for mensaje in mensajes:
        sys.stdout.write('\r' + mensaje)
        sys.stdout.flush()
        time.sleep(0.3)
    
    print("\n")
    print("╔════════════════════════════════════════╗")
    print("║                                        ║")
    print("║     ¡Gracias por usar el sistema!     ║")
    print("║          ¡Buen vuelo! ✈️               ║")
    print("║                                        ║")
    print("╚════════════════════════════════════════╝")
    print()

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
                        print(f"Costo: ${asiento.tipo.calcularCosto():,.0f} COP")
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
                print("\n--- Actualizar Horas de Vuelo ---")
                print("Puede ingresar:")
                print("  • Número decimal: 2.5, 3.75, etc.")
                print("  • Formato 12 horas: 2:30 PM, 8:00 AM, etc.")
                print("  • Solo horas: 3 PM, 10 AM, etc.")
                
                entrada = input("\nIngrese las horas de vuelo a agregar: ")
                horas = convertir_hora_12_a_24(entrada)
                avion.horasVuelo += horas
                print(f"✓ Horas de vuelo actualizadas: {avion.horasVuelo:.2f} horas")
            except ValueError as e:
                print(f"✗ Error: Formato no válido. Ejemplos: '2.5', '3:30 PM', '8 AM'")
                
        elif opcion == "8":
            animacion_cierre()
            break
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    print("Bienvenido al Sistema de Gestión de Aviones")
    main()
