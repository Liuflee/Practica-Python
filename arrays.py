import random as rd
import numpy as np

array = np.array([rd.randint(1,100) for i in range(10)])
minim = array[0]
maxim = array[0]
suma = 0

for num in array:
    if num < minim:
        minim = num
    if num > maxim:
        maxim = num
    suma += num

print(f"Numero mayor: {maxim}")
print(f"Numero menor: {minim}")
print(f"Suma        : {suma}")
print(f"Promedio    : {suma/len(array)}")
print(array)