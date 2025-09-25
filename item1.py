dispositivos = {
    'Router 1801': 0,
    'Router 2901': 0,
    'Router 2911': 0,
    'Router 4321': 0,
    'Router 4331': 0,
    'Switch 2960': 0,
    'Switch 3550': 0,
    'Switch 3560': 0,
    'Switch 9200': 0,
    'Access Point Serie Catalyst 9100': 0,
    'Access Point Serie Catalyst 9800': 0,
    'Access Point Serie Catalyst 4800': 0,
    'WLS Controladora Wireless Cisco 3504': 0
}

def mostrar_informe():
    print("\nInforme de dispositivos:")
    for dispositivo, cantidad in dispositivos.items():
        if cantidad > 0:
            print(f"{dispositivo}: {cantidad}")

def pedir_cantidad_dispositivo():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
            else:
                return cantidad
        except ValueError:
            print("Por favor ingrese un número entero válido.")

def agregar_dispositivo():
    while True:
        print("\nDispositivos disponibles:")
        for idx, dispositivo in enumerate(dispositivos.keys(), 1):
            print(f"{idx}. {dispositivo}")
        
        opcion = input("\nSeleccione el número del dispositivo que desea agregar (o 'Salir' para finalizar): ")
        
        if opcion.lower() == 'salir' or opcion == 'S' or opcion == 's':
            print("\n¡Proceso finalizado!")
            return False  # Termina la función y permite mostrar el informe final
        
        if opcion.isdigit() and 1 <= int(opcion) <= len(dispositivos):
            dispositivo_seleccionado = list(dispositivos.keys())[int(opcion) - 1]
            print(f"\nHa seleccionado: {dispositivo_seleccionado}")
            
            cantidad = pedir_cantidad_dispositivo()
            
            dispositivos[dispositivo_seleccionado] += cantidad
            print(f"\nSe han agregado {cantidad} unidades de {dispositivo_seleccionado}.")
        else:
            print("\nOpción no válida. Intente de nuevo.")
        
        continuar = input("\n¿Desea agregar otro dispositivo? (s/n): ").lower()
        if continuar != 's':
            break  # Si no desea seguir agregando dispositivos, sale del ciclo
    return False  # Termina el proceso y permite mostrar el informe final

def main():
    print("Bienvenido al programa de gestión de dispositivos de red de la empresa.")
    
    while True:
        if not agregar_dispositivo():  # Si el usuario elige 'Salir', termina el ciclo
            break
    
    mostrar_informe()  # Muestra el informe final después de que el usuario termina de agregar dispositivos
    
    print("\n¡Gracias por usar el programa!")
if __name__ == '__main__':
    main()

