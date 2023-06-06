'''Crear un arreglo de dos dimensiones de 3 x 3 con números ceros,
excepto la diagonal principal que debe contener en el mismo orden los
siguientes elementos 1, 2 y 3.'''

import numpy as np

array = np.zeros([3, 3], dtype=int)

print("Array inicial con ceros")
print(array)

#Rellena las diagonales con un rango entre 1, hasta el largo del arreglo + 1
np.fill_diagonal(array, [i for i in range(1, (len(array.diagonal()) + 1))]) 

print("\nArray Final")
print(array)