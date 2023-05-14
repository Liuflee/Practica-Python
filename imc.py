imc = 0
while imc == 0:
    try:
        peso = int(input("Ingrese su peso en Kg: "))
    except:
        print("Solo debe ingresar numeros enteros")
    else:
        if peso <= 10:
            print("Usted es un pitufo, o no existe")
        else:
            while True:
                try:
                    altura = float(input("Ingrese su altura en metros: "))
                    if 0.0 < altura < 3.0:
                        imc = peso / (altura)**2
                        break
                    else:
                        print("La altura debe ser menor a 3 metros y mayor a 0")
                except:
                    print("Ingrese numeros reales")

print(f"Su indice de masa corporal es {imc:.1f}")