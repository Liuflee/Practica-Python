DUOC_CHORIPAN = 1200
DUOC_ITALIANO = 1500
DUOC_VEGANO = 2000

opcion_principal = ""
opcion_comida = 0
total = 0

while opcion_principal != 'c':
    print("\n" + "=" * 50)
    print("\t\tSandwichería el Duocano")
    print("=" * 50)
    print("a - Realizar Venta")
    print("b - Cerrar Turno")
    print("c - Salir")
    try:
        opcion_principal = input("\nIngrese una opción: ").lower()
        if not opcion_principal.isalpha():
            raise ValueError()
    except ValueError:
        print("Opción inválida. Ingrese una letra dentro de las opciones.")
    else:
        if opcion_principal == 'a':
            print("\n" + "=" * 50)
            print("\t\tOpciones")
            print("=" * 50)
            print("1 - Duoc Choripán $1200")
            print("2 - Duoc Italiano $1500")
            print("3 - Duoc Vegano   $2000")
            print("\n4 - Volver atrás")
            while opcion_comida != 4:
                try:
                    opcion_comida = int(input("\nIngrese una opción: "))
                except ValueError:
                    print("Debe ingresar números enteros.")
                else:
                    if opcion_comida in (1, 2, 3):
                        if opcion_comida == 1:
                            total += DUOC_CHORIPAN
                            print("\nDUOC Choripán añadido al total")
                        elif opcion_comida == 2:
                            total += DUOC_ITALIANO
                            print("\nDUOC Italiano añadido al total")
                        elif opcion_comida == 3:
                            total += DUOC_VEGANO
                            print("\nDUOC Vegano añadido al total")
                    elif opcion_comida == 4:
                        print("\nRegresando al menú")
                    else:
                        print("\nOpción fuera de rango.")
        elif opcion_principal == "b":
            print(f"\nTurno cerrado. El total recaudado es: ${total}")
            cerrar_caja_opciones = ("s", "si")
            cerrar_caja = input("\n¿Quiere reiniciar la compra? (S): ").lower()
            if cerrar_caja in cerrar_caja_opciones:
                total = 0
                print("\nEl total se ha reiniciado.")
print("\n¡Hasta luego!")
