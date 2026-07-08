codigos = [1, 2, 3, 4, 5, 6, 7]
nombres = ["Hamburguesa", "Papas Fritas", "Pizza", "Empanada", "Gaseosa", "Agua", "Helado"]
precios = [3500, 2000, 5500, 900, 1500, 1000, 2200]

total_recaudado = 0
cantidad_pedidos = 0

def mostrar_menu_productos():
    print("\n--- PRODUCTOS DISPONIBLES ---")
    i = 0
    while i < len(codigos):
        print(f"{codigos[i]} - {nombres[i]} - ${precios[i]}")
        i = i + 1

def buscar_precio(codigo):
    i = 0
    while i < len(codigos):
        if codigos[i] == codigo:
            return precios[i]
        i = i + 1
    return -1

def armar_pedido():
    subtotal_pedido = 0
    seguir = True
    mostrar_menu_productos()
    
    while seguir == True:
        # Aquí si ponen una 'A', el programa muere
        codigo = int(input("Ingrese código de producto (0 para terminar): "))
        
        if codigo == 0:
            seguir = False
        else:
            precio = buscar_precio(codigo)
            if precio == -1:
                print("Error: código inexistente.")
            else:
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad > 0:
                    subtotal_pedido = subtotal_pedido + (precio * cantidad)
                    print(f"Agregado correctamente.")
                else:
                    print("Cantidad no válida.")
    return subtotal_pedido

def main():
    global total_recaudado, cantidad_pedidos
    continuar = True
    while continuar == True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1 - Realizar pedido")
        print("2 - Ver estadísticas")
        print("3 - Salir")
        opcion = int(input("Seleccione una opción: ")) # Riesgo de caída del sistema
        
        if opcion == 1:
            subtotal = armar_pedido()
            if subtotal > 0:
                if subtotal > 10000:
                    subtotal = subtotal * 0.90
                total_recaudado = total_recaudado + subtotal
                cantidad_pedidos = cantidad_pedidos + 1
                print(f"Pedido cobrado: ${subtotal}")
        elif opcion == 2:
            print(f"\nPedidos del día: {cantidad_pedidos}")
            print(f"Total Recaudado: ${total_recaudado}")
        elif opcion == 3:
            continuar = False
            print("¡Hasta luego!")

main()
