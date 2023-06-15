import numpy as np
import random as rd

# Funciones
class OutOfRange(Exception):
    def __init__(self, msg):
        self.msg = msg

def calculate_iva(amount):
    IVA = 0.19
    total = amount * IVA
    print(f"El monto final es {total}")
    return (total)

def calculate_discount(amount, discount):
    total = amount - (amount * discount / 100)
    print(f"El precio es ${total}")
    return total

def calculate_imc(weight, height):
    imc = weight / height**2
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


def validation(data_type, msg, min_value=0, max_value=10e20):
    while True:
        try:
            amount = data_type(input(msg))
            if (min_value < amount < max_value):
                break
            else:
                raise OutOfRange(f"Ingrese un numero mayor a {min_value} y menor a {max_value}")
        except ValueError:
            print(f"Error: Ingrese un número {data_type.__name__}")
        except OutOfRange as e:
                print("Error:", e.msg)
    return amount

def menu(options):
    print("-" * 50)
    print("\t\tMenú")
    print("-" * 50)
    for enum, option in enumerate(options):
        print(f"{enum+1} - {option}")
    print("-" * 50)
    while True:
        try:
            chosen_option = int(input("Ingrese una opción: "))
            if 1 <= chosen_option <= len(options):
                break
            else:
                raise OutOfRange("Ingrese una opción dentro del rango")
        except ValueError:
            print("-" * 50)
            print("Error: Ingrese un numero entero")
            print("-" * 50)
        except OutOfRange as e:
            print("-" * 50)
            print("Error:", e)
            print("-" * 50)
    return chosen_option

def create_array(shape):
    array = np.array([[rd.randint(100, 200) for i in range(shape)] for j in range(shape)])
    return array

def create_sum_array(array1, array2):
    array_final = np.add(array1, array2)
    return array_final

def string_decorator(string=None):
    if string is not None:
        print("-" * 60)
        print(string)
    print("-" * 60)