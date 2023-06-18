'''Crear un programa que contenga un menú con las siguientes opciones:
• Área de un circulo
• Perímetro de un cuadrado
Ingrese los valores necesarios para calcular y entregar 
resultados utilizando funciones.'''

import functions_circle as fn

opc = 0

opciones_menu = [
    "Calcular Área de circulo",
    "Perimetro de un cuadrado",
    "Salir"
]

while opc != 3:
    opc = fn.menu(opciones_menu)
    if opc == 1:
        print("-" * 50)
        radio = fn.validation(float, "Ingrese el radio del circulo: ")
        fn.area_circulo(radio)
    if opc == 2:
        print("-" * 50)
        lado = fn.validation(float, "Ingrese el valor de los lados del cuadrado: ")
        fn.perimetro_cuadrado(lado)

print("Hasta luego")            