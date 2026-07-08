print("\n--- BIENVENIDO AL SISTEMA DE PEDIDOS ---")

subtotal_pedido = 0
continuar_pedido = True

while continuar_pedido == True:
    print("\n--- PRODUCTOS DISPONIBLES ---")
    print("1 - Hamburguesa ($3500)")
    print("2 - Papas Fritas ($2000)")
    print("3 - Pizza ($5500)")
    print("0 - Terminar pedido")
    
    codigo = int(input("Ingrese código de producto: "))
    
    if codigo == 0:
        continuar_pedido = False
    elif codigo == 1:
        cantidad = int(input("Ingrese cantidad: "))
        subtotal_pedido = subtotal_pedido + (3500 * cantidad)
    elif codigo == 2:
        cantidad = int(input("Ingrese cantidad: "))
        subtotal_pedido = subtotal_pedido + (2000 * cantidad)
    elif codigo == 3:
        cantidad = int(input("Ingrese cantidad: "))
        subtotal_pedido = subtotal_pedido + (5500 * cantidad)
    else:
        print("Código inválida.")

# Descuento simple
if subtotal_pedido > 10000:
    descuento = subtotal_pedido * 0.10
    subtotal_pedido = subtotal_pedido - descuento
    print(f"Descuento del 10% aplicado.")

print(f"\nTotal final a pagar: ${subtotal_pedido}")
print("¡Gracias por su compra!")
