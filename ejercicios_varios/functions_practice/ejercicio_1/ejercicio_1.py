'''
Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
1 - Calcular_iva
2 - Descuento
3 - Calcular_Imc
'''

import functions as fn

def main():
          
    menu_option = 0
    options = [
        "Calcular IVA",
        "Calcular descuento",
        "Calcular IMC",
        "Salir"
    ]

    while menu_option != 4:
        menu_option = fn.menu(options)
        if menu_option == 1:
            iva_amount = fn.validation(int, msg="Ingrese el monto a calcular: ")
            fn.calculate_iva(iva_amount)
        elif menu_option == 2:
            discount_amount = fn.validation(int, msg="Ingrese el monto a calcular: ")
            discount = fn.validation(float, msg="Ingrese el descuento a calcular: ", max_value=100)
            fn.calculate_discount(discount_amount, discount)
        elif menu_option == 3:
            weight = fn.validation(int, msg="Ingrese su peso (kg): ")
            height = fn.validation(float, msg="Ingrese su altura (m): ")
            fn.calculate_imc(weight, height)
    print("Hasta luego")

if __name__ =="__main__":
    main()

