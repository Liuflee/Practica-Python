'''Escribir una función que reciba otra función y una lista
y devuelva otra lista con el resultado de aplicar la función
dada a cada uno de los elementos de la lista.'''

def funcionInicial(funcion, lista):
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def duplicar(iteracion): 
    return iteracion + iteracion

listaInput = [1, 2, 3, 4]

print(funcionInicial(duplicar, listaInput))

