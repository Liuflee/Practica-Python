'''Desarrolle un algoritmo que permita ingresar notas y sus respectivas ponderaciones
finalizado el ingreso calcule el promedio.
Realice las validaciones necesarias.'''

promedio = 0
suma_ponderacion = 0

while True:
    try:
        nota = float(input("Ingrese una nota entre 1 y 7: "))
    except ValueError:
        print("Solo se deben ingresar numeros")
    else:
        if 1 <= nota <= 7:
            while True:
                try:
                    ponderacion = int(input("Ingrese la ponderación de la nota sin (%): "))
                    if suma_ponderacion + ponderacion > 100:
                        print(f"La suma de las ponderaciones no puede ser mayor a 100. La actual es: {suma_ponderacion}")
                    elif 0 < ponderacion <= 100:
                        suma_ponderacion += ponderacion
                        promedio += nota * ponderacion
                        break
                    
                except ValueError:
                    print("Solo se deben ingresar numeros enteros para la ponderación")
    
    if suma_ponderacion == 100:
        break

if suma_ponderacion == 0:
    print("No se ingresaron notas")
else:
    promedio /= suma_ponderacion
    print(f"El promedio ponderado es: {promedio:.1f}") 