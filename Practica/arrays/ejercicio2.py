'''Utilice las siguientes funciones en el arreglo creado en el punto 1
• Promedio de los elementos.
• Suma de los elementos.
• Mostrar el elemento mayor.
• Mostrar el elemento menor.
• Mostrar sólo los elementos de la diagonal principal'''

import numpy as np
import random as rd

array = np.array([[rd.randint(0, 100) for i in range(3) ] for j in range(3)])
print(array)

print(f"Promedio: {array.mean():.1f}")
print(f"Suma de los elementos: {array.sum()}")
print(f"Elemento mayor: {array.max()}")
print(f"Elemento menor: {array.min()}")
print(f"Diagonal: {np.diagonal(array)}") 

#También se puede hacer de esta forma:

'''filas, columnas = array.shape

for i in range(filas):
    for j in range(columnas):
     if i == j:
        print(array[i, j])'''

