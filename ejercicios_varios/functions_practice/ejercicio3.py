'''En una cafetería se venden 4 tipos de cafés: 
Espresso 			$1.500 
Capuchino 		$1.800 
Latte 			$1.600 
Moca 			$1.700 
Determine el total a pagar por un cliente que puede llevar varios cafés y aplique el descuento del 10% al total a pagar,
 si su compra es superior o igual a $3.000.
Considere crear un menú de opciones y calcule el monto utilizando función.

'''
import functions as fn

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
    opc = fn.menu()
    if opc in range(1, 5):

        cafe_seleccionado = list(precios.keys())[opc - 1]
        precio_cafe = precios[cafe_seleccionado]
        total_cafe += precio_cafe
        print(f"{cafe_seleccionado}  ${precio_cafe} añadido al total: ${total_cafe}")

    elif opc == 5:
        total_cafe = 0
        print("\nCompra reiniciada el total es 0")
        
if total_cafe >= 3000:
    total_final = calculate_discount(total_cafe, DESCUENTO)
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
