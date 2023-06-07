'''Crear un programa que contenga un menú con las siguientes opciones:
• Área de un circulo
• Perímetro de un cuadrado
Ingrese los valores necesarios para calcular y entregar 
resultados utilizando funciones.'''

import math

class OutOfRange(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def area_circulo(radio):
    area = (math.pi * radio**2)
    print(f"El área del circulo es: {area:.1f}")
    return area

def perimetro_cuadrado(lado):
    perimetro = (4 * lado)
    print(f"El perimetro del cuadrado es: {perimetro:.1f}")
    return perimetro

opc = 0
while opc != 3:
    print("1 - Calcular Área del circulo")
    print("2 - Calcular Perimetro del cuadrado")
    print("3 - Salir")
    try:
        opc = int(input("Ingrese una opción: "))
        if opc not in (1, 2, 3):
            raise OutOfRange("Debe ingresar un numero dentro del rango")
    except ValueError:
        print("Error: Ingrese un numero entero")
    except OutOfRange as e:
        print("Error:", e.mensaje)
    else:
        if opc == 1:
            while True:
                try:
                    radio = float(input("Ingrese el radio: "))
                    if radio < 0:
                        raise OutOfRange("Debe ingresar un numero dentro del rango")
                    else:
                        area_circulo(radio)
                        break
                except ValueError:
                    print("Error: Ingrese un numero entero")
                except OutOfRange as e:
                    print("Error:", e.mensaje)
        if opc == 2:
            while True:
                try:
                    lado = float(input("Ingrese el valor de los lados: "))
                    if lado < 0:
                        raise OutOfRange("Debe ingresar un numero dentro del rango")
                    else:
                        perimetro_cuadrado(lado)
                        break
                except ValueError:
                    print("Error: Ingrese un numero entero")
                except OutOfRange as e:
                    print("Error:", e.mensaje)
print("Hasta luego")
