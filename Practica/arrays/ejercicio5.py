'''Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive, luego esos
números serán las dimensiones de un arreglo bidimensional.
 Posteriormente
 poblar la matriz con números reales. Finalmente, muestre:
 • El arreglo poblado.
 • La suma por filas.
 • El promedio por columnas'''

import numpy as np
import random as rd

while True:
    try:
        fila = int(input("\nIngrese las columnas del array entre 3 y 6: "))
        if fila not in (3, 4, 5, 6):
            raise ValueError()
    except ValueError:
        print("\nIngrese un numero entero entre 3 y 6")
    else:
        while True:
            try:
                columna = int(input("\nIngrese las filas del arreglo entre 3 y 6: "))
                if columna not in (3, 4, 5, 6):
                    raise ValueError()
                else:
                    break
            except ValueError:
               print("\nIngrese un numero entero entre 3 y 6") 
        break

arreglo = np.array([[rd.uniform(0.0, 100.0) for i in range(fila)] for j in range(columna)])

print(f"\nArreglo:\n{arreglo}")
print(f"\nSuma de cada fila: {np.sum(arreglo, axis=1)}")
print(f"\nPromedio de cada columna: {np.mean(arreglo, axis=0)}")
