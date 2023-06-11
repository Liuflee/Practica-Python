num = int(input("Ingrese un numero: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} no es un numero primo")
            break
    else:
        print(f"{num} es un numero primo")
else:
    print(f"{num} no es un numero primo")
