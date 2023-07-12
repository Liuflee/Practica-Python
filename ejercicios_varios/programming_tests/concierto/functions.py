import numpy as np

def crear_array():
    array = np.zeros((10, 10), dtype=int)
    return array

def imprimir_array(array):

    print("-" * 50)
    print(" ", end=" ")
    for j in range(len(array[0])):
        print(f" {j}", end="")
    print()

    for i, row in enumerate(array):
        if i < 10:
            print(f" {i}", end=" ")
        else:
            print(i, end=" ")

        for seat in row:
            if seat == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()

def validar(tipo, mensaje, min, max):
    while True:
        try:
            opc = tipo(input(mensaje))
            if min <= opc <= max:
                return opc
            else:
                print(f"Error: Ingrese un numero entre {min} y {max}")
        except ValueError:
            print(f"Error: Ingrese un numero de tipo {tipo.__name__}")

def tipos_asientos(fila):
    RANGOS = {
        (0, 1): "Platinum",
        (2, 4): "Gold",
        (5, 9): "Silver"
    }
    for rango, tipo in RANGOS.items():
        if rango[0] <= fila <= rango[1]:
            return tipo

def calcular_precio(tipo):
    PRECIOS = {
        "Platinum": 120000,
        "Gold": 80000,
        "Silver": 50000
    }
    return PRECIOS.get(tipo, 0)

def comprar_entradas(array, rut_array):
    cantidad = validar(int, "Ingrese la cantidad de entradas: ", 1, 3)
    for _ in range(cantidad):
        imprimir_array(array)
        while True:
            fila = validar(int, "Ingrese la columna del asiento", 0, 9)
            columna = validar(int, "Ingrese la fila del asiento", 0, 9)
            if array[fila][columna] == 0:
                rut = validar(int, "Ingrese el rut del ocupante: ", 1000000, 999999999)
                tipo_de_asiento = tipos_asientos(fila)
                print("Reserva realizada correctamente")
                print(f"El tipo de asiento es {tipo_de_asiento} y su valor es {calcular_precio(tipo_de_asiento)} ")
                continuar = input("Desea continuar con la compra?(s / n): ")
                if continuar.lower() in ("s", "si"):
                    print("Compra exitosa")
                    rut_array[fila][columna] = rut
                    array[fila][columna] = 1
                    break
                else:
                    print("Compra cancelada")
                    return
            else:
                print("El asiento ya está ocupado")
                elegir_otro = print("Desea elegir otro asiento?: ")
                if elegir_otro.lower() in ("no", "n"):
                    print("Compra cancelada")
                    return

def mostrar_asistentes(ruts):
    ruts_nuevos = []
    for i in ruts:
        for j in i:
            if j != 0:
                ruts_nuevos.append(j)

    ruts_nuevos.sort()
    for i in ruts_nuevos:
        print(i)
            
def mostrar_ganancias(array):
    
    contador_pl = 0
    contador_gold = 0
    contador_sil = 0

    for i, fila in enumerate(array):
        for _, asiento in enumerate(fila):
            if asiento == 1:
                tipos_de_asiento = tipos_asientos(i)
                if tipos_de_asiento == "Platinum":
                    contador_pl += 1
                elif tipos_de_asiento == "Gold":
                    contador_gold += 1
                else:
                    contador_sil += 1
    
    total_silver = contador_sil * calcular_precio("Silver")
    total_gold = contador_gold * calcular_precio("Gold")
    total_pl = contador_pl * calcular_precio("Platinum")
    total = total_gold + total_pl + total_silver

    print("-" * 50)
    print("Ganancias totales:")
    print("-" * 50)
    print("Tipo de asiento\t\t   Cantidad\t\tTotal")
    print(f"Asiento Silver\t\t\t{contador_sil}\t\t{total_silver}")
    print(f"Asiento Gold\t\t\t{contador_gold}\t\t{total_gold}")
    print(f"Asiento Platinum\t\t{contador_pl}\t\t{total_pl}")
    print(f"Total\t\t\t\t{contador_sil + contador_gold + contador_pl}\t\t{total}")
    print("-" * 50)

def menu(opciones):
    for enum, i in enumerate(opciones):
        print(f"{enum + 1} - {i}")
    opcion = validar(int, "Ingrese una opción: ", 1, len(opciones))
    return opcion

