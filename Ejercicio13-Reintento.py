'''Desarrolle un algoritmo que permita ingresar notas y sus respectivas ponderaciones
finalizado el ingreso calcule el promedio.
Realice las validaciones necesarias.'''

promedio = 0
suma_ponderacion = 0

while True:
    try:
        nota = float(input("Ingrese una nota entre 1 y 7: "))
        if 1 <= nota <= 7:
            ponderacion = int(input("Ingrese la ponderación de la nota sin (%): "))
            if suma_ponderacion + ponderacion > 100:
                print("La suma de las ponderaciones no puede ser mayor a 100.")
            elif 0 < ponderacion <= 100:
                suma_ponderacion += ponderacion
                promedio += nota * ponderacion
                if suma_ponderacion == 100:
                    break
    except ValueError:
        print("Solo se deben ingresar numeros")

if suma_ponderacion == 0:
    print("No se ingresaron notas")
else:
    promedio /= suma_ponderacion
    print(f"El promedio ponderado es: {promedio:.2f}")
