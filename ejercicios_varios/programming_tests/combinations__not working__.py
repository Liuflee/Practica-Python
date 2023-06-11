def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

def listas(lista1, lista2):
    listaFinal = []
    for i in lista1:
        for j in lista2:
            combinaciones = factorial(i) // (factorial(i-j) * factorial(j))
            listaFinal.append(combinaciones)
    return listaFinal

listaN1 = [2, 3, 5, 6]
listaN2 = [5, 3, 2, 9]

print(listas(listaN1, listaN2))
