DESCUENTO_AUXILIAR = 0.15
DESCUENTO_ADMINISTRATIVO = 0.1
DESCUENTO_DOCENTE = 0.05

PRECIO_CARILLAS = 250000
PRECIO_IMPLANTES = 475000
PRECIO_BRACKETS = 850000

contador_carillas = 0
contador_implantes = 0
contador_brackets = 0

porcentaje = 0
total_nd = 0
total = 0
flag = 0

opcion_principal = 0
while opcion_principal != 3:
    print("\tClinica Dental")
    print("1 - Cotización")
    print("2 - Renunciar")
    print("3 - Salir")
    try:
        opcion_principal = int(input("Ingrese una opción: "))
        if opcion_principal not in (1, 2, 3):
            print("Ingrese una opción dentro del rango")

    except ValueError:
        print("Error: Ingrese un numero entero")
    else:
        if opcion_principal == 1:
            print("\tCargo")
            print("1 - Trabajador Auxiliar")
            print("2 - Trabajador Administrativo")
            print("3 - Trabajador Docente")
            print("4 - Volver Atrás")

            opcion_descuento = 0
            while opcion_descuento != 4:
                if flag == 1:
                    break
                try:
                    opcion_descuento = int(input("Ingrese su cargo: "))
                except ValueError:
                    print("Error: Ingrese un numero entero")
                else:
                    if opcion_descuento in (1, 2, 3):
                        if opcion_descuento == 1:
                            descuento = DESCUENTO_AUXILIAR
                            
                        elif opcion_descuento == 2:
                            descuento = DESCUENTO_ADMINISTRATIVO
                            
                        else:
                            descuento = DESCUENTO_DOCENTE
                        print("\tTratamientos")
                        print("1 - Carillas Porcelana - $250.000")
                        print("2 - Implantes Dentales - $475.000")
                        print("3 - Ortodoncia Brackets - $800.000")
                        print("4 - Mostrar Cotización Total")
                        print("5 - Volver Atrás")

                        opcion_tratamiento = 0
                        while opcion_tratamiento != 4:
                            if flag == 1:
                                break
                            try:
                                opcion_tratamiento = int(input("Ingrese una opción: "))
                            except ValueError:
                                print("Error: Ingrese un numero entero: ")
                            else:
                                if opcion_tratamiento in (1, 2, 3):
                                    if opcion_tratamiento == 1:
                                        total_nd += PRECIO_CARILLAS
                                        contador_carillas += 1
                                    elif opcion_tratamiento == 2:
                                        total_nd += PRECIO_IMPLANTES
                                        contador_implantes += 1
                                    else:
                                        total_nd += PRECIO_BRACKETS
                                        contador_brackets += 1
                                elif opcion_tratamiento == 4:
                                    flag = 1
                                    total = total_nd - (total_nd * descuento)
                                    print("-" * 50)
                                    print("\t\tCotización")
                                    print("-" * 50)
                                    if contador_carillas != 0:
                                        print(f"--> {contador_carillas} tratamiento(s) Carillas Porcelana ${PRECIO_CARILLAS * contador_carillas}")
                                    if contador_implantes != 0:
                                        print(f"--> {contador_implantes} tratamiento(s) Implantes Dentales ${PRECIO_IMPLANTES * contador_implantes}")
                                    if contador_brackets != 0:
                                        print(f"--> {contador_brackets} tratamiento(s) Ortodoncia Brackets ${PRECIO_BRACKETS * contador_brackets}")
                                    print("-" * 50)
                                    print(f"Subtotal\t\t  ${total_nd}")
                                    print(f"Descuento {descuento * 100}% \t ${total_nd * descuento}")
                                    print("-" * 50)
                                    print(f"Total\t\t\t${total}")
                                    print("-" * 50)
                                    print(f"Son 12 cuotas de:\t ${(total / 12):.1f}")
                                    print("\n¡Sonría bonito!")
                                elif opcion_tratamiento == 5:
                                    print("\nVolviendo atrás")
                                else:
                                    print("Error: Opción fuera del rango")
                    elif opcion_descuento == 4:
                        print("Regresando al menú anterior")
                    else:
                        print("Error: Opción fuera del rango")
    
        elif opcion_principal == 2:
            renuncia = input("¿Quiere Hacer una nueva cotización y eliminar la anterior? (s / si): ").lower()
            if renuncia in ("s", "si"):
                print("Cotización reiniciada")
                total_nd = 0
                descuento = 0
                contador_brackets = 0
                contador_carillas = 0
                contador_implantes = 0
                flag = 0
        elif opcion_principal == 3:
            print("Hasta luego")
        