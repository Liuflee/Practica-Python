'''Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive, luego esos
números serán las dimensiones de un arreglo bidimensional.
 Posteriormente
 poblar la matriz con números reales. Finalmente, muestre:
 • El arreglo poblado.
 • La suma por filas.
 • El promedio por columnas'''

import functions as fn
import numpy as np

class OutOfRange(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


fila = fn.validation(int, "Ingrese las columnas del arreglo entre 3 y 6: ", min_value=2, max_value=7)
print("-" * 60)
columna = fn.validation(int, "Ingrese las columnas del arreglo entre 3 y 6: ", min_value=2, max_value=7)
print("-" * 60)

arreglo = fn.create_array(fila, columna)

print("-" * 60)

print("Arreglo:\n")
print(arreglo)

print("-" * 60)

print("Promedio de las columnas:\n")
fn.mean_by_column(arreglo)

print("-" * 60)

print("Sumas de las filas:\n")
fn.sum_by_row(arreglo)
