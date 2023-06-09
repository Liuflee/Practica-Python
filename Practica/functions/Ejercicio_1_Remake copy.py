'''Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
Calcular_Iva
Descuento
Calcular_Imc'''

import funciones as fn

def main():        
    opc = 0
    opciones = [
        "Calcular IVA",
        "Calcular descuento",
        "Calcular IMC"
    ]

    while opc != 4:
        opc = fn.menu(opciones)
        if opc == 1:
            monto_iva = fn.validacion(int, mensaje="Ingrese el monto a calcular: ")
            fn.calcular_iva(monto_iva)
        elif opc == 2:
            monto_desc = fn.validacion(int, mensaje="Ingrese el monto a calcular: ")
            descuento = fn.validacion(float, mensaje="Ingrese el descuento a calcular: ", maximo=1)
            fn.calcular_descuento(monto_desc, descuento)
        elif opc == 3:
            peso = fn.validacion(int, mensaje="Ingrese su peso: ")
            altura = fn.validacion(float, mensaje="Ingrese su altura: ")
            fn.calcular_imc(peso, altura)
    print("Hasta luego")

if __name__ =="__main__":
    main()

