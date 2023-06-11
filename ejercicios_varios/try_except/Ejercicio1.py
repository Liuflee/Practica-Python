'''Ejercicio 1
Considere el caso anterior y aplique:
Try y except donde corresponda
En la opción 1, indique si un número ingresado es par o impar
En la opción 2, muestre la serie 
Fibonacci de los primeros 10 números
La opción 3, es Salir de la aplicación'''

while True:
    try:
        opcion = int(input("\nElija una opción:\n1 - Saber si un numero es par o impar\n2 - Fibonacci\n3 - Salir\n"))
        
        if opcion == 1:
            num = int(input("\nIngrese un numero: "))
            if num % 2 == 0:
                print("\nEl numero ingresado es par\n")
            else:
                print("\nEl numero es impar\n")
        elif opcion == 2:
            fibonacci = [0, 1] 
            for i in range(2, 10): 
                fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
            print(f"\n{fibonacci}\n")

        elif opcion == 3:
            print("\nHasta luego!")
            break
        else:
            print("\nOpción no válida\n")
    except ValueError:
        print("\nEl valor ingresado no es valido\n")
