import funciones as fn
pedidos = []

while True:
    try:
        print("**** Menu Reparto Paquetes PaquExpress ****")
        print("1. Registrar Pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        opcionMenu = int(input("Ingrese opcion: "))

        if opcionMenu == 1:
            fn.registrar_pedido(pedidos)

        elif opcionMenu == 2:
            fn.listar_todos_los_pedidos(pedidos)


        elif opcionMenu == 3:
            fn.imprimir_hoja_de_ruta(pedidos)

        elif opcionMenu == 4:
            print("Saliendo del programa")
            break

        else:
            print("Por favor ingrese opcion válida")
        print("")
    except ValueError:
        print("Por favor ingrese solo números")

