cont = 0
acum = 0

num1 = int(input("Ingrese num 1: "))
num2 = int(input("Ingrese num 2: "))
num3 = int(input("Ingrese num 3: "))

def numeros(num):
    global cont, acum
    if num % 2 == 0 and num > 0:
        acum = acum + num1
    else:
        cont = cont + 1

numeros(num1)
numeros(num2)
numeros(num3)

print(f"La suma de numeros pares mayores a 0 es: {acum} y la cantidad de numeros impares o menores a 0 es: {cont}")
