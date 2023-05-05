'''Ejercicio 2
En un delivery se venden 4 tipos de pan:
• Amasado $1.500
• Molde $1.000
• Baguette $2.000
• Integral $3.000
Determine el total a pagar por un cliente, el cual puede comprar
diferentes tipos y cantidad de pan.
o Si el total de la venta es superior a $5000 el envío es gratis, sino
se cobra el 10% adicional.
Muestre los mensajes correspondientes.'''

PRECIO_AMASADO = 1500
PRECIO_MOLDE = 1000
PRECIO_BAGUETTE = 2000
PRECIO_INTEGRAL = 3000

total = 0

def totalPan(precio):
    cantidad = int(input("\n¿Cuantos kilos va a querer?: "))
    if cantidad < 0:
        print("\nCantidad no valida\n")
        return 0
    else:
        return (cantidad * precio)

while True:
    try:
        opcion = int(input("\nElija una opción:\n1 - Pan Amasado\n2 - Molde\n3 - Baguette\n4 - Integral\n5 - Terminar compra\n6 - Reiniciar compra\n"))
        if opcion == 1:
            total += totalPan(PRECIO_AMASADO)
        elif opcion == 2:
            total += totalPan(PRECIO_MOLDE)
        elif opcion == 3:
            total += totalPan(PRECIO_BAGUETTE)
        elif opcion == 4:
            total += totalPan(PRECIO_INTEGRAL)
        elif opcion == 5:
            break
        elif opcion == 6:
            print("\nCompra reiniciada\n")
            total = 0
        else:
            print("\nOpción no válida\n")
    except ValueError:
        print("\nEl valor ingresado no es valido\n")


if total != 0:
    if total > 5000:
        print("\nTiene envio gratis")

    else:
        print(f"\nSe le cobra un 10% adicional")
        total = total * 1.10

    print(f"\nSu total es: {round(total)}")
else:
    print("\nCompra cancelada")