cont = 0
while True:
    try:
        num1 = int(input("Ingrese num 1: "))
        num2 = int(input("Ingrese num 2: "))
        num3 = int(input("Ingrese num 3: "))
    except ValueError:
        print("Debes ingresar un numero entero")
    else:
        if num1 < 0:
            cont += 1
        if num2 < 0:
            cont += 1
        if num3 < 0:
            cont += 1
        print(f"La cantidad de numeros menores a 0 es {cont}")
        break
