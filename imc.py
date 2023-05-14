'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros)
calcule el índice de masa corporal y lo almacene en una variable.
Luego, debe mostrar por pantalla la frase: “Tu índice de masa corporal es:{imc}”
No olvide validar'''

imc = 0

while imc == 0: #Ciclo while general
    try:
        peso = int(input("Ingrese su peso en Kg: "))
    except: #Try-Except para el peso
        print("Solo debe ingresar numeros enteros")
    else:
        if peso <= 0: #Validación del peso
            print("Usted es un pitufo, o no existe")
        else:
            while True: #Ciclo while para la altura y el calculo del IMC
                try:
                    altura = float(input("Ingrese su altura en metros: "))
                    if 0.0 < altura < 3.0:
                        imc = peso / (altura)**2 #Calculo del IMC
                        break 
                    else:
                        print("La altura debe ser menor a 3 metros y mayor a 0")
                except: #Try-Except para la altura
                    print("Ingrese numeros reales")

print(f"Su indice de masa corporal es {imc:.1f}") #print final, redondea el valor de imc con :.1f