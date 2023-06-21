import numpy as np

COMMON_PRICE = 60000
LEGS_PRICE = 80000
NON_RECLINABLE_PRICE = 50000

RANGES = {
    (0, 4): "espacio adicional para piernas",
    (5, 8): "común",
    (9, 10): "no reclinable",
    (11, 12): "espacio adicional para piernas",
    (13, 32): "común",
}

seats = np.zeros((33, 6), dtype=int)
passengers_rut = np.zeros((33, 6), dtype=int)

class OutOfRange(Exception):
    def __init__(self, message):
        self.message = message

def validation(data_type, msg, min_value=float('-inf'), max_value=float('inf')):
    while True:
        try:
            print("-" * 50)
            amount = data_type(input(msg))
            
            if min_value <= amount <= max_value:
                break
            else:
                print("-" * 50)
                raise OutOfRange(f"Ingrese un número mayor o igual a {min_value} y menor o igual a {max_value}")

        except ValueError:
            print("-" * 50)
            print(f"Error: Ingrese un número {data_type.__name__}")
            print("-" * 50)
        except OutOfRange as e:
            print("-" * 50)
            print("Error:", e.message)
            print("-" * 50)
    return amount

def get_seat_type(row):
    for seat_range, seat_type in RANGES.items():
        if seat_range[0] <= row <= seat_range[1]:
            return seat_type
    return "común"

def show_seats_condition():
    print("-" * 50)
    print(" ", end=" ")
    for j in range(len(seats[0])):
        print(f" {j}", end="")
    print()

    for i, row in enumerate(seats):
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


def buy_tickets():
    tickets_numbers = validation(int, "Ingrese la cantidad de tickets a comprar: ", 0, 33*6)
    for _ in range(tickets_numbers):
        show_seats_condition()
        while True:
            row = validation(int, "Ingrese la fila del asiento: ", 0, 32)
            column = validation(int, "Ingrese la columna del asiento: ", 0, 5)
            if seats[row][column] == 0:
                rut = validation(int, "Ingrese el RUT del pasajero: ", 1000000, 999999999)
                passengers_rut[row][column] = rut
                seat_type = get_seat_type(row)
                print("-" * 50)
                print(f"Reserva realizada correctamente. El asiento es de tipo {seat_type}")
                print("-" * 50)
                confirm_purchase = input("¿Desea confirmar la compra? (Si/No): ")
                if confirm_purchase.lower() == "si":
                    print("-" * 50)
                    print("Compra confirmada.")
                    seats[row][column] = 1
                    break
                else:
                    print("-" * 50)
                    print("Compra cancelada.")
                    return
            else:
                print("El asiento ya está ocupado. Por favor, elija otro")
                choose_another = input("¿Desea elegir otro asiento? (Si/No): ")
                if choose_another.lower() == "no":
                    print("Compra cancelada.")
                    return

def show_passengers_list():
    passengers = []
    for row in passengers_rut:
        for rut in row:
            if rut != 0:
                passengers.append(rut)
    
    passengers.sort()
    print("-" * 50)
    print("Listado de pasajeros:")
    for rut in passengers:
        print("-" * 50)
        print(rut)

def find_passenger():
    rut_to_search = validation(int, "Ingrese el RUT del pasajero: ", 1000000, 999999999)
    
    for i, row in enumerate(passengers_rut):
        for j, rut in enumerate(row):
            if rut == rut_to_search:
                print("-" * 50)
                print("El pasajero se encuentra en el asiento:", i, j)
                return
    print("-" * 50)
    print("El pasajero no se encuentra registrado")

def change_seats():
    row = validation(int, "Ingrese la fila del asiento a reasignar: ", 0, 32)  
    column = validation(int, "Ingrese la columna del asiento a reasignar: ", 0, 5) 
    
    if seats[row][column] == 1:
        new_rut = validation(int, "Ingrese el RUT del nuevo pasajero: ", 1000000, 999999999)
        passengers_rut[row][column] = new_rut
        print("-" * 50)
        print("Asiento reasignado correctamente.")
    else:
        print("-" * 50)
        print("El asiento no está ocupado")

def show_total():
    normal_count = 0
    legs_count = 0
    non_reclinable_count = 0
    
    for i, row in enumerate(seats):
        for _, seat in enumerate(row):
            if seat == 1:
                seat_type = get_seat_type(i)
                if seat_type == "espacio adicional para piernas":
                    legs_count += 1
                elif seat_type == "no reclinable":
                    non_reclinable_count += 1
                else:
                    normal_count += 1
    
    normal_total = normal_count * COMMON_PRICE
    legs_total = legs_count * LEGS_PRICE
    non_reclinable_total = non_reclinable_count * NON_RECLINABLE_PRICE
    total = normal_total + legs_total + non_reclinable_total
    
    print("-" * 50)
    print("Ganancias totales:")
    print("-" * 50)
    print("Tipo de asiento\t\t   Cantidad\t\tTotal")
    print(f"Asiento común\t\t\t{normal_count}\t\t{normal_total}")
    print(f"Asiento espacio para piernas\t{legs_count}\t\t{legs_total}")
    print(f"Asiento no reclinable\t\t{non_reclinable_count}\t\t{non_reclinable_total}")
    print(f"Total\t\t\t\t{normal_count + legs_count + non_reclinable_count}\t\t{total}")
    print("-" * 50)

def menu(options):
    print("-" * 50)
    print("\t\tMenú")
    print("-" * 50)
    for enum, option in enumerate(options):
        print(f"{enum+1} - {option}")
    print("-" * 50)
    while True:
        try:
            chosen_option = int(input("Ingrese una opción: "))
            if 1 <= chosen_option <= len(options):
                break
            else:
                raise OutOfRange("Ingrese una opción dentro del rango")
        except ValueError:
            print("-" * 50)
            print("Error: Ingrese un número entero")
            print("-" * 50)
        except OutOfRange as e:
            print("-" * 50)
            print("Error:", e.message)
            print("-" * 50)
    return chosen_option

