'''Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive, luego esos
números serán las dimensiones de un arreglo bidimensional.
 Posteriormente
 poblar la matriz con números reales. Finalmente, muestre:
 • El arreglo poblado.
 • La suma por filas.
 • El promedio por columnas'''

import numpy as np
import random as rd

class OutOfRange(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

while True:
    try:
        print("\n")
        fila = int(input("Ingrese las columnas del array entre 3 y 6: "))
        print("-" * 60)
        if fila not in (3, 4, 5, 6):
            raise OutOfRange("Ingrese un numero entre 3 y 6")
    except ValueError:
        print("\nError: Ingrese un numero entero")
    except OutOfRange as e:
        print("\nError:", e)
    else:
        while True:
            try:
                columna = int(input("Ingrese las filas del arreglo entre 3 y 6: "))
                print("-" * 60)
                if columna not in (3, 4, 5, 6):
                    raise OutOfRange("Ingrese un numero entre 3 y 6")
                else:
                    break
            except ValueError:
                print("\nError: Ingrese un numero entero")
            except OutOfRange as e:
                print("\nError:", e)
        break

arreglo = np.array([[round(rd.uniform(0.0, 100.0), 2) for i in range(fila)] for j in range(columna)])

print("Arreglo:\n")
print(arreglo)
print("-" * 60)

print("Sumas de las filas:\n")
filas_final = np.sum(arreglo, axis=1)
for i in range(len(filas_final)):
    print(F"Suma de la fila numero {i + 1}: {filas_final[i]:.2f}")
print("-" * 60)

print("Promedio de las columnas:\n")
columnas_final = np.mean(arreglo, axis=0)
for i in range(len(columnas_final)):
    print(F"Promedio de la columna numero {i + 1}: {columnas_final[i]:.2f}")
print("-" * 60)