import time

EURO_DOLAR = 1.11
LIBRA_EURO = 1.12

TIPOS_CAMBIO = {
    'A': EURO_DOLAR,
    'B': 1 / EURO_DOLAR,
    'C': LIBRA_EURO,
    'D': 1 / LIBRA_EURO
}

divisa_origen = ''

while not divisa_origen:
    print("¿Qué divisa quieres cambiar?")
    time.sleep(0.3)
    print("A - Euro a Dolar")
    time.sleep(0.3)
    print("B - Dolar a Euro")
    time.sleep(0.3)
    print("C - Libra a Euro")
    time.sleep(0.3)
    print("D - Euro a Libra")
    divisa = input().upper()

    if divisa in TIPOS_CAMBIO:
        divisa_origen = divisa
    else:
        print("Opción incorrecta\n")

if divisa_origen in ('A', 'D'):
    divisa_origen_texto = 'euros'
elif divisa_origen == 'B':
    divisa_origen_texto = 'dólares'
else:
    divisa_origen_texto = 'libras'

time.sleep(0.3)
cantidad = float(input("Introduce la cantidad de {} que quieres cambiar: ".format(divisa_origen_texto)))
tipo_cambio = TIPOS_CAMBIO[divisa_origen]
monto = cantidad * tipo_cambio

if divisa_origen in ('A', 'B'):
    divisa_destino = 'dólares' if divisa_origen == 'A' else 'euros'
else:
    divisa_destino = 'euros' if divisa_origen == 'C' else 'libras'

time.sleep(0.3)
print("\nEl monto en {} es: {}\n".format(divisa_destino, round(monto, 2)))

time.sleep(0.3)
input("Presione \"enter\" para salir...")
