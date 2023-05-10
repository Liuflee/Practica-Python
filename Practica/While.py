num = int(input("Ingresa un numero: "))

divisores = 0
contador = 1

while contador <= num:
    if num % contador == 0:
        divisores += 1
    contador += 1

if divisores == 2:
    print(f"{num} es un numero primo")
else:
    print(f"{num} no es un numero primo")
    