promedio = 0.0
suma_ponderacion = 0.0

while True:

    try:
        nota = float(input("\nIngrese su nota: "))
        if nota < 1.0 or nota > 7.0:
            print("\nError: La nota debe estar entre 1.0 y 7.0")
            continue

        ponderacion = float(input("\nIngrese la ponderación de la nota sin (%): "))
        if ponderacion <= 0.0 or ponderacion >= 100.0:
            print("\nLa ponderación debe estar entre 0 y 100")
            continue

        if suma_ponderacion + ponderacion > 100.0:
            print("\nLa ponderación acumulada no puede superar el 100%")
            continue

        promedio += nota * ponderacion
        suma_ponderacion += ponderacion

        if suma_ponderacion == 100.0:
            break

    except ValueError:
        print("\nError: Debe ingresar un numero valido")

if suma_ponderacion == 0.0:
    print("\nDebe ingresar al menos una nota con ponderación")
else:
    promedio /= suma_ponderacion
    print(f"\nEl promedio ponderado es: {promedio:.2f}")
