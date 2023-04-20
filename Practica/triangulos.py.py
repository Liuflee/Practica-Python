try:
    lado1 = int(input("Ingrese lado 1: "))
    lado2 = int(input("Ingrese lado 2: "))
    lado3 = int(input("Ingrese lado 3: "))
except ValueError:
    print("Debes ingresar un numero entero")
else:
    if lado1 <0 or lado2<0 or lado3 < 0:
        print("El numero debe ser positivo")
    elif lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        if lado1 == lado2 == lado3:
            print("El triangulo es equilatero")
        elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
            print("El triangulo es isosceles")
        else:
            print("El triangulo es escaleno")
    else:
        print("No se puede formar un triangulo con los lados ingresados")