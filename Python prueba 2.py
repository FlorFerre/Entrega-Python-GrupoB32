codigos = [1, 2, 3, 4, 5, 6, 7]
nombres = ["Hamburguesa", "Papas Fritas", "Pizza", "Empanada", "Gaseosa", "Agua", "Helado"]
precios = [3500, 2000, 5500, 900, 1500, 1000, 2200]

total_recaudado = 0
cantidad_pedidos = 0

ejecutando_sistema = True

while ejecutando_sistema == True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1 - Realizar pedido")
    print("2 - Ver estadísticas del día")
    print("3 - Salir")
    opcion = int(input("Seleccione una opción: "))
    
    if opcion == 1:
        # Lógica para un pedido
        subtotal_pedido = 0
        armando = True
        
        # Mostrar productos
        print("\n--- PRODUCTOS DISPONIBLES ---")
        i = 0
        while i < len(codigos):
            print(f"{codigos[i]} - {nombres[i]} - ${precios[i]}")
            i = i + 1
            
        while armando == True:
            codigo = int(input("Ingrese código de producto (0 para terminar): "))
            
            if codigo == 0:
                armando = False
            else:
                # Buscar en listas paralelas
                posicion = -1
                i = 0
                while i < len(codigos):
                    if codigos[i] == codigo:
                        posicion = i
                    i = i + 1
                
                if posicion == -1:
                    print("Error: El código no existe.")
                else:
                    cantidad = int(input("Ingrese cantidad: "))
                    if cantidad <= 0:
                        print("Error: cantidad inválida.")
                    else:
                        importe = precios[posicion] * cantidad
                        subtotal_pedido = subtotal_pedido + importe
                        print(f"Agregado: {nombres[posicion]} x{cantidad}")
                        
        # Aplicar descuento e incrementar generales
        if subtotal_pedido > 0:
            if subtotal_pedido > 10000:
                subtotal_pedido = subtotal_pedido * 0.90
            
            print(f"Total de este pedido: ${subtotal_pedido}")
            total_recaudado = total_recaudado + subtotal_pedido
            cantidad_pedidos = cantidad_pedidos + 1
            
    elif opcion == 2:
        print("\n--- ESTADÍSTICAS ---")
        print(f"Pedidos: {cantidad_pedidos}")
        print(f"Total: ${total_recaudado}")
        
    elif opcion == 3:
        ejecutando_sistema = False
        print("Saliendo...")
    else:
        print("Opción inválida.")
        