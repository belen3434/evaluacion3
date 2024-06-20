sectores = ["centro","norte","sur"]


def registrar_pedido(pedidos):
    print("Registro de pedidos")
    
    while True: 
        nombre = input("Ingrese nombre y apellido: ")
        if nombre == "":
            print("Por favor ingrese un nombre")
        else:
            break
    while True:
        direccion = input("Ingrese direccion: ")
        if direccion == "":
            print("Por favor ingrese una dirección")
        else:
            break
    while True:
        sector = input("Ingrese sector (centro/norte/sur): ").lower()
        if sector in sectores:
            break
        else:
            print("Por favor ingrese el sector (centro/norte/sur)")

    acumuladorPequeño = 0
    acumuladorMediano = 0
    acumuladorGrande = 0    

    while True:
        print("**** Menu Paquetes ****")
        print("1. Paquete Pequeño")
        print("2. Paquete Mediano")
        print("3. Paquete Grande")
        print("4. Salir")
        opcionPaquete = int(input("Ingrese opcion: "))

        if opcionPaquete != 4:
            cantidadPaquetes = int(input("Ingrese cantidad paquetes: "))

        if opcionPaquete == 1:
            acumuladorPequeño = acumuladorPequeño + cantidadPaquetes
        
        elif opcionPaquete == 2:
            acumuladorMediano = acumuladorMediano + cantidadPaquetes

        elif opcionPaquete == 3:
            acumuladorGrande = acumuladorGrande + cantidadPaquetes
        
        elif opcionPaquete == 4:
            break
        
        else:
            print("Por favor ingrese opcion válida")

    pedido = {
        "Nombre" : nombre,
        "Direccion" : direccion,
        "Sector" : sector,
        "PaquetePequeño" : acumuladorPequeño,
        "PaqueteMediano" : acumuladorMediano,
        "PaqueteGrande" : acumuladorGrande
    }

    pedidos.append(pedido)


def listar_todos_los_pedidos(pedidos):
    print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Nombre","Direccion","Sector","PaquetePequeño","PaqueteMediano","PaqueteGrande"))
    print("=" * 100)

    for pedido in pedidos:
        print("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(pedido["Nombre"],pedido["Direccion"],pedido["Sector"],pedido["PaquetePequeño"],pedido["PaqueteMediano"],pedido["PaqueteGrande"]))

def imprimir_hoja_de_ruta(pedidos):
    with open("hoja_de_ruta.txt","w") as archivo:
        archivo.write("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Nombre","Direccion","Sector","PaquetePequeño","PaqueteMediano","PaqueteGrande"))
        archivo.write("\n")

        for pedido in pedidos:
            archivo.write("{:<20} {:<15} {:<15} {:<15} {:<15} {:<15}".format(pedido["Nombre"],pedido["Direccion"],pedido["Sector"],pedido["PaquetePequeño"],pedido["PaqueteMediano"],pedido["PaqueteGrande"]))
            archivo.write("\n")

    print("Pedido Completado")