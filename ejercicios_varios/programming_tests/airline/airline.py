import functions as fn


def main():
    
    options = [
    "Comprar pasajes",
    "Mostrar ubicaciones disponibles",
    "Ver listado de pasajeros",
    "Buscar pasajero",
    "Reasignar asiento",
    "Mostrar ganancias totales",
    "Salir"
]
    
    while True:
        chosen_option = fn.menu(options)
        if chosen_option == 1:
            fn.buy_tickets()
        elif chosen_option == 2:
            fn.show_seats_condition()
        elif chosen_option == 3:
            fn.show_passengers_list()
        elif chosen_option == 4:
            fn.find_passenger()
        elif chosen_option == 5:
            fn.change_seats()
        elif chosen_option == 6:
            fn.show_total()
        elif chosen_option == 7:
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
