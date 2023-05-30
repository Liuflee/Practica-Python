'''Ingresar dos números enteros, valídelos y luego determinar y mostrar:

i. Si el primero es divisible por el segundo

ii. Si el segundo es divisible por el primero

iii. Cuál de los dos es mayor; en caso de que sean iguales, mostrar mensaje adecuado

iv. Si ambos son impares'''

while True:
    try:
        num1 = int(input("Ingrese el primer numero: "))
        if num1 == 0:
            raise ZeroDivisionError("El primer numero no puede ser cero")
        while True:
            try:
                num2 = int(input("Ingrese el segundo numero: "))
                if num2 == 0:
                    raise ZeroDivisionError("El segundo numero no puede ser cero")
                else:
                    break
            except ValueError:
                print("Error: Debe ingresar numeros enteros que no sean 0")
                continue
            except ZeroDivisionError as e:
                print("Error", e)
                continue
    except ValueError:
        print("Error: Debe ingresar numeros enteros que no sean 0")
    except ZeroDivisionError as e:
        print("Error:", e)

    else:
        if num1 % num2 == 0:
            print("El numero 1 es divisible por el segundo numero")
        else:
            print("El numero 1 NO es divisble por el segundo")

        if num2 % num1 == 0:
            print("El numero 2 es divisible por el primer numero")
        else:
            print("El numero 2 NO es divisible por el primer numero")

        if num1 < num2:
            print("El numero 1 es menor que el numero 2")
        elif num1 == num2:
            print("Ambos numeros son iguales")
        else:
            print("El numero 2 es menor que el numero 1")

        if not (num1 % 2 == 0) and not (num2 % 2 == 0):
            print("Ambos numeros son impares")
        break

