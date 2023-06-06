'''Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
Calcular_Iva
Descuento
Calcular_Imc'''

class OutOfRange(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def calcular_iva(monto):
    IVA = 0.19
    monto_final_iva = monto * IVA
    print(f"El monto final es {monto_final_iva}")
    return (monto_final_iva)

def calcular_descuento(monto, descuento):
    monto_final_desc = monto - (monto * descuento)
    print(f"El monto final es {monto_final_desc}")
    return monto_final_desc

def calcular_imc(peso, altura):
    imc = peso / altura**2
    if 0 < imc <= 18.5:
        print(f"{imc:.1f}: Bajo Peso")
    elif imc <= 24.9:
        print(f"{imc:.1f}: Adecuado")
    elif imc <= 29.9:
        print(f"{imc:.1f}: Sobrepeso")   
    elif imc <= 34.9:
        print(f"{imc:.1f}: Obesidad Grado 1")
    elif imc <= 39.9:
        print(f"{imc:.1f}: Obesidad Grado 2")
    else:
        print(f"{imc:.1f}: Obesidad Grado 3")
    return (imc)

opc = 0
while opc != 4:
    print("1 - Calcular IVA")
    print("2 - Calcular monto con descuento")
    print("3 - Calcular IMC")
    print("4 - Salir")
    try:
        opc = int(input("Ingrese una opción: "))
        if opc not in (1, 2, 3, 4):
            raise OutOfRange("Debe ingresar un numero dentro del rango")
    except ValueError:
        print("Error: Ingrese un numero entero")
    except OutOfRange as e:
        print("Error:", e.mensaje)
    else:
        if opc == 1:
            while True:
                try:
                    monto_iva = int(input("Ingrese el monto a calcular: "))
                    if monto_iva < 0:
                        raise OutOfRange("Ingrese un numero mayor a cero")
                    else:
                        calcular_iva(monto_iva)
                        break
                except ValueError:
                    print("Error: Ingrese un numero entero")
                except OutOfRange as e:
                      print("Error:", e.mensaje)
        elif opc == 2:
            while True:
                try:
                    monto_desc = int(input("Ingrese el monto a calcular: "))
                    if monto_desc < 0:
                        raise OutOfRange("Ingrese un numero mayor a cero")
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese un numero entero")
                except OutOfRange as e:
                      print("Error:", e)
            while True:
                try:
                    descuento = float(input("Ingrese el descuento para calcular: "))
                    if descuento < 0:
                        raise OutOfRange("Ingrese un numero mayor a cero")
                    else:
                        calcular_descuento(monto_desc, descuento)
                        break
                except ValueError:
                    print("Error: Ingrese un numero real")
                except OutOfRange as e:
                      print("Error:", e)
        elif opc == 3:
            while True:
                try:
                    peso = int(input("Ingrese su peso: "))
                    if peso < 0:
                        raise OutOfRange("Ingrese un numero mayor a cero")
                    else:
                        break
                except ValueError:
                    print("Error: Ingrese un numero entero")
                except OutOfRange as e:
                      print("Error:", e)
            while True:
                try:
                    altura = float(input("Ingrese su altura: "))
                    if altura < 0:
                        raise OutOfRange("Ingrese un numero mayor a cero")
                    else:
                        calcular_imc(peso, altura)
                        break
                except ValueError:
                    print("Error: Ingrese un numero real")
                except OutOfRange as e:
                      print("Error:", e)
print("Hasta luego")