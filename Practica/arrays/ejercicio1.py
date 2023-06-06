'''Crear un arreglo de dos dimensiones de tamaño 3 x 3, con elementos
aleatorios de números enteros del 0 al 100.'''


import numpy as np
import random as rd

array = np.array([[rd.randint(0, 100) for i in range(3) ] for j in range(3)])
print(array)