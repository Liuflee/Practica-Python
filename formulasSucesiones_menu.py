def buscar_posicion(termino, buscar, distancia): 
    posicion = (buscar - termino) / distancia + 1
    print(buscar, "Tiene la posición", posicion)

def buscar_primer_termino(termino, posicion, distancia):
    inicial = termino - (posicion - 1) * distancia
    print(f"El termino inicial es {inicial}")

def calcular_termino(inicial, posicion, distancia):
    termino = inicial + (posicion - 1) * distancia
    print(f"El termino en la posición {posicion}, es: {termino}")

while True:
    try:
        print("¿Que desea hacer?")
        print("1 - Buscar la posición en la que está un termino")
        print("2 - Buscar el valor en una posición")
        print("3 - Buscar el primer termino")
        print("4 - Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion not in (1, 2, 3, 4):
            raise Exception("Ingrese un numero dentro del rango")
        else:
            if opcion == 1:
                while True:
                    try:
                        inic = float(input("Ingrese el termino inicial: "))
                        termino_a_buscar = float(input("Ingrese el termino a buscar: "))
                        distancia = float(input("Ingrese la distancia entre un numero y otro: "))
                        buscar_posicion(inic, termino_a_buscar, distancia)
                        break
                    except:
                        print("Ingrese un numero ")
            elif opcion == 2:
                while True:
                    try:
                        inic = float(input("Ingrese el termino inicial: "))
                        posicion = float(input("Ingrese la posicion a buscar: "))
                        distancia = float(input("Ingrese la distancia entre un numero y otro: "))
                        calcular_termino(inic, posicion, distancia)
                        break
                    except:
                        print("Ingrese un numero ")
            elif opcion == 3:
                while True:
                    try:
                        termino = float(input("Ingrese el termino que tiene: "))
                        posicion = float(input("Ingrese la posicion a buscar: "))
                        distancia = float(input("Ingrese la distancia entre un numero y otro: "))
                        buscar_primer_termino(termino, posicion, distancia)
                        break
                    except:
                        print("Ingrese un numero ")
            else:
                print("Hasta Luego")
                break
    except:
        print("ERROR")
