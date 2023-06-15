'''Ejercicio 4: Escribir una función que reciba dos arrays y 
devuelva un nuevo array con la suma de los indices en la misma posición de cada array.'''

import functions as fn

def main():

    fn.string_decorator("Ejercicio 4")
    shape = fn.validation(int, "Ingrese el tamaño de los arreglos (Máximo 10): ", max_value= 11)
    array = fn.create_array(shape)
    fn.string_decorator("Array 1:")
    print(array)
    fn.string_decorator("Array 2:")
    array2 = fn.create_array(shape)
    print(array2)
    fn.string_decorator("Array final:")
    print(fn.create_sum_array(array, array2))
    fn.string_decorator()

if __name__ == '__main__':
    main()

