
class OutOfRange(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def calcular_iva(monto):
    IVA = 0.19
    monto_final_iva = monto * IVA
    print(f"El monto final es {monto_final_iva}")
    return (monto_final_iva)

def calcular_descuento(monto, descuento):
    monto_final_desc = monto - (monto * descuento)
    print(f"El monto final es {monto_final_desc}")
    return monto_final_desc

def calcular_imc(peso, altura):
    imc = peso / altura**2
    if 0 < imc <= 18.5:
        print(f"{imc:.1f}: Bajo Peso")
    elif imc <= 24.9:
        print(f"{imc:.1f}: Adecuado")
    elif imc <= 29.9:
        print(f"{imc:.1f}: Sobrepeso")   
    elif imc <= 34.9:
        print(f"{imc:.1f}: Obesidad Grado 1")
    elif imc <= 39.9:
        print(f"{imc:.1f}: Obesidad Grado 2")
    else:
        print(f"{imc:.1f}: Obesidad Grado 3")
    return (imc)

def validacion(tipo_dato, mensaje, minimo=0):
    while True:
        try:
            monto = tipo_dato(input(mensaje))
            if monto < minimo:
                raise OutOfRange("Ingrese un numero mayor a {minimo}")
            else:
                break
        except ValueError:
            print(f"Error: Ingrese un numero {tipo_dato}")
        except OutOfRange as e:
                print("Error:", e.mensaje)
    return monto

def area_circulo(radio):
    import math
    area = (math.pi * radio**2)
    print(f"El área del circulo es: {area:.1f}")
    return area

def perimetro_cuadrado(lado):
    perimetro = (4 * lado)
    print(f"El perimetro del cuadrado es: {perimetro:.1f}")
    return perimetro

def menu(opciones):
    print("-" * 50)
    print("\t\tMenú")
    print("-" * 50)
    for i, opcion in enumerate(opciones):
        print(f"{i+1} - {opcion}")
    print("-" * 50)
    while True:
        opcion_elegida = input("Ingrese una opción: ")
        if opcion_elegida.isdigit():
            opcion_elegida = int(opcion_elegida)
            if 1 <= opcion_elegida <= len(opciones):
                break
        print("-" * 50)
        print("Opción inválida. Intente nuevamente.")
        print("-" * 50)
    return opcion_elegida

