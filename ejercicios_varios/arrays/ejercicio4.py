'''Declarar y poblar un arreglo unidimensional de largo 10 con números enterospositivos,
utilizando la función random,
luego ingrese un número e indique si éste seencuentra en el arreglo'''

import numpy as np
import random as rd

arreglo = np.array([rd.randint(0, 100) for i in range(10)])

while True:
    try:
        num = int(input("Ingrese un numero entre 0 y 100: "))
        if not 0 <= num <= 100:
            raise ValueError()
    except:
        print("Error: Ingrese un numero entero dentro del rango")
    else:
        if num in arreglo:
            print(f"El numero {num} se encuentra en el arreglo")
        else:
            print("No se encontró el numero en el arreglo")
        break   

