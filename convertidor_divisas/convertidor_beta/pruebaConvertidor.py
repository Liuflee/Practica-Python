
euro_dolar = 1.11
libra_euro = 1.12

divisa = input("¿Qué divisa quieres cambiar?: \nA - Euro a Dolar\nB - Dolar a Euro\nC - Libra a Euro\nD - Euro a Libra\n")

divisa = divisa.upper()

if divisa == 'A':
    divisa_origen = 'euros'
    texto = input("Introduce la cantidad de {} que quieres cambiar: ".format(divisa_origen))
elif divisa == 'B':
    divisa_origen = 'dólares'
    texto = input("Introduce la cantidad de {} que quieres cambiar: ".format(divisa_origen))
elif divisa == 'C':
    divisa_origen = 'libras'
    texto = input("Introduce la cantidad de {} que quieres cambiar: ".format(divisa_origen))
elif divisa == 'D':
    divisa_origen = 'euros'
    texto = input("Introduce la cantidad de {} que quieres cambiar: ".format(divisa_origen))
else:
    divisa_origen = ' '



if divisa == "A":
    cantidad = float(texto)
    print("El monto en dolares es: {}".format(round((cantidad * euro_dolar), 2)))
elif divisa == "B":
    cantidad = float(texto)
    print("El monto en euros es: {}".format(round((cantidad / euro_dolar), 2)))
elif divisa == "C":
    cantidad = float(texto)
    print("El monto en euros es: {}".format(round((cantidad * libra_euro), 2)))
elif divisa == "D":
    cantidad = float(texto)
    print("El monto en libras es: {}".format(round((cantidad / libra_euro), 2)))
else:
    print("Opción incorrecta")

print("\n")

input("Presione enter para salir...")