import functions as fn

def main():
    options = ["Ingresar vehículo", "Mostrar vehículos", "Modificar precio/kilometraje", "Vender auto", "Salir"]
    principal = [[], [], [], [], [], [], [], [], [], [], [], []]
    menu_opc = fn.menu(options)
    while menu_opc != 5:
        if menu_opc == 1:
            fn.add_car(principal)
        elif menu_opc == 2:
            fn.show_cars(principal)
        elif menu_opc == 3:
            fn.modify_car(principal)
        elif menu_opc == 4:
            fn.sell_car(principal)
        menu_opc = fn.menu(options)

if __name__ == "__main__":
    main()
