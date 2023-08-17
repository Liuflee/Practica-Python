def buscar_posicion(termino, buscar, distancia): 
    posicion = (buscar - termino) / distancia + 1
    print(buscar, "Tiene la posición", posicion)

def buscar_primer_termino(termino, posicion, distancia):
    inicial = termino - (posicion - 1) * distancia
    print(f"El termino inicial es {inicial}")

def calcular_termino(inicial, posicion, distancia):
    termino = inicial + (posicion - 1) * distancia
    print(f"El termino en la posición {posicion}, es: {termino}")

buscar_posicion(3, 333, 6)
calcular_termino(3, 20, 6)
calcular_termino(3, 30, 6)