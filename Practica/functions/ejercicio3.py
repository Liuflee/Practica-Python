'''En una cafetería se venden 4 tipos de cafés: 
Espresso 			$1.500 
Capuchino 		$1.800 
Latte 			$1.600 
Moca 			$1.700 
Determine el total a pagar por un cliente que puede llevar varios cafés y aplique el descuento del 10% al total a pagar,
 si su compra es superior o igual a $3.000.
Considere crear un menú de opciones y calcule el monto utilizando función.

'''
class OutOfRange(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def descuento(monto, descuento):
    monto_final = monto - (monto * descuento)
    return monto_final

precios = {
    "Espresso": 1500,
    "Capuccino": 1800,
    "Latte": 1600,
    "Moca": 1700
}

total_cafe = 0
opc = 0
DESCUENTO = 0.1

print("\nBienvenid@ a Code Brew")
while opc != 6:
    print("#" * 50)
    print("\tMenú:")
    print("#" * 50)
    for i, (cafe, precio) in enumerate(precios.items(), start=1):
        print(f"{i} - {cafe}   | ${precio}")
        
    print("#" * 50)
    print("5 - Reiniciar compra")
    print("6 - Terminar  compra")
    print("#" * 50)
    try:
        opc = int(input("Ingrese una opción: "))
        if opc not in range(1, 7):
            raise OutOfRange("\nDebe ingresar un numero dentro del rango")
    except ValueError:
        print("\nError: Ingrese un numero entero")
    except OutOfRange as e:
        print("\nError:", e.mensaje)
    else:
        if opc in range(1, 5):
            cafe_seleccionado = list(precios.keys())[opc - 1]
            precio_cafe = precios[cafe_seleccionado]
            total_cafe += precio_cafe
            print(f"{cafe_seleccionado}  ${precio_cafe} añadido al total: ${total_cafe}")
        elif opc == 5:
            total_cafe = 0
            print("\nCompra reiniciada el total es 0")

if total_cafe >= 3000:
    total_final = descuento(total_cafe, DESCUENTO)
    print("#" * 50)
    print("\tGracias por comprar")
    print("#" * 50)
    print("¡Tienes un descuento del 10%!")
    print("#" * 50)
    print(f"El total a pagar es: ${total_final:.1f}")
elif total_cafe > 0:
    print("#" * 50)
    print(f"El total a pagar es: ${total_cafe:.1f}")
else:
    print("#" * 50)
    print(f"\nCompra cancelada")
