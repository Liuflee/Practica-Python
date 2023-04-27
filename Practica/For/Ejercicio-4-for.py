num = int(input("Ingrese un numero: "))
contDivisores = 0

for i in range(1, num):
    if (num % i) == 0:
        contDivisores += i

if contDivisores == num:
    print(f"{num} es un numero perfecto")
else:
    print(f"{num} no es un numero perfecto")
