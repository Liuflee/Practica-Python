DUOC_CHORIPAN = 1200
DUOC_ITALIANO = 1500
DUOC_VEGANO = 2000

opc_principal = ""
opcion_comida = 0
total = 0

while opc_principal != 'c':
    print("+" * 50)
    print("\tSandwichería el Duocano")
    print("+" * 50)
    print("a - Realizar Venta")
    print("b - Cerrar Turno")
    print("c - Salir")
    try:
        opc_principal = input("Ingrese una opción: ").lower()
        if not opc_principal.isalpha():
            raise Exception()
    except:
        print("Opción invalida. Ingrese una letra dentro de las opciones")
    else:
        if opc_principal == 'a':
            print("+" * 50)
            print("\tOpciones")
            print("+" * 50)
            print("1 - Duoc Choripán $1200")
            print("2 - Duoc Italiano $1500")
            print("3 - Duoc Vegano   $2000")
            print("4 - Volver atrás")
            while opcion_comida != 4:
                try:
                    opcion_comida = int(input("\nIngrese una opción: "))
                except:
                    print("Debe ingresar numeros enteros")
                else:
                    if opcion_comida in (1, 2, 3, 4):
                        if opcion_comida == 1:
                            total += DUOC_CHORIPAN
                        elif opcion_comida == 2:
                            total += DUOC_ITALIANO
                        elif opcion_comida == 3:
                            total += DUOC_VEGANO
                    else:
                        print("Opción fuera de rango")
        elif opc_principal == "b":
                print(f"Turno cerrado. El total recaudado es {total}")
                cerrar_caja_opciones = ("s", "si")
                cerrar_caja = input("¿Quiere cerrar la caja? (S): ").lower()
                if cerrar_caja in cerrar_caja_opciones:
                    total = 0
                    print("El total se ha reiniciado")
print("¡Hasta Luego!")




           