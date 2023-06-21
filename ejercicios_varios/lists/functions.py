class OutOfRange(Exception):
    def __init__(self, message):
        self.message = message  

def validation_rut():
    while True:
        try:
            rut = int(input("Ingrese el rut: "))
            if 5000000 < rut < 50000000:
                if len(str(rut)) > 8:
                    print("El rut no puede tener más de 9 dígitos")
                elif len(str(rut)) < 8:
                    print("El rut no puede tener menos de 9 dígitos")
                else:
                    break
            else:
                print("El rut ingresado no es válido")
        except ValueError:
            print("Error: Ingrese un número entero")
                                                        
    return rut

def validation(data_type, msg, min_value=float('-inf'), max_value=float('inf')):
    while True:
        try:
            amount = data_type(input(msg))
            if (min_value < amount < max_value):
                break
            else:
                raise OutOfRange(f"Ingrese un número mayor a {min_value} y menor a {max_value}")
        except ValueError:
            print(f"Error: Ingrese un número {data_type.__name__}")
        except OutOfRange as e:
            print("Error:", e.message)
    return amount

def validation_phone():
    while True:
        try:
            phone = input("Ingrese el telefono: ")
            if len(str(phone)) > 9:
                print("El telefono no puede tener más de 9 dígitos")
            elif len(str(phone)) < 9:
                print("El telefono no puede tener menos de 9 dígitos")
            else:
                break
        except ValueError:
            print("Error: Ingrese un número entero")
        
    return phone

def email_validation():
    while True:
        email = input("Ingrese el correo: ")
        if len(email) < 6:
            print("El correo debe tener como mínimo 6 caracteres")
            
        elif "@" not in email:
            print("El correo debe tener un @")
            
        elif "." not in email:
            print("El correo debe tener un .")
            
        else:
            break
    return email

def patent_validation(list_principal):
    while True:
        patent = input("Ingrese la patente: ")
        if patent not in list_principal[4] and len(patent) == 6:
            break
        else:
            print("La patente ya existe o no es válida")
    return patent

def fuel_validation():
    while True:
        fuel = input("Ingrese el tipo de combustible: ")
        if fuel.lower() in ("diesel", "kerosene"):
            break
        else:
            print("El tipo de combustible no es válido")
    return fuel

def doors_validation():
    while True:
        try:
            doors = int(input("Ingrese la cantidad de puertas: "))
            if doors == 2 or doors == 4:
                break
            else:
                raise OutOfRange("Ingrese 2 o 4 puertas")
        except ValueError:
            print("Error: Ingrese un número entero")
        except OutOfRange as e:
            print("Error:", e.message)
    return doors
            
def transmission_validation():
    while True:
        transmission = input("Ingrese el tipo de transmisión: ")
        if transmission.lower() in ("m", "a"):
            break
        else:
            print("El tipo de transmisión no es válido")
    return transmission


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

def add_car(list_principal):
    print("-" * 50)
    print("\t\tIngresar vehículo")
    print("-" * 50)
    name = input("Ingrese el nombre del propietario: ")
    rut = validation_rut()
    phone = validation_phone()
    email = email_validation()
    patent = patent_validation(list_principal)
    year = validation(int, "Ingrese el año: ", 1900, 2022)
    fuel = fuel_validation()
    doors = doors_validation()
    transmission = transmission_validation()
    color = input("Ingrese el color: ")
    km = validation(int, "Ingrese el kilometraje: ", 0)
    price = validation(int, "Ingrese el precio: ", 0)
    list_principal[0].append(name)
    list_principal[1].append(rut)
    list_principal[2].append(phone)
    list_principal[3].append(email)
    list_principal[4].append(patent)
    list_principal[5].append(year)
    list_principal[6].append(fuel)
    list_principal[7].append(doors)
    list_principal[8].append(transmission)
    list_principal[9].append(color)
    list_principal[10].append(km)
    list_principal[11].append(price)
    print("-" * 50)
    print("Vehículo ingresado con éxito")
    print("-" * 50)

def show_cars(list_principal):
    print("-" * 50)
    print("\t\tMostrar vehículos")
    print("-" * 50)
    for i in range(len(list_principal[0])):
        print(f"Nombre: {list_principal[0][i]}")
        print(f"Rut: {list_principal[1][i]}")
        print(f"Teléfono: {list_principal[2][i]}")
        print(f"Correo: {list_principal[3][i]}")
        print(f"Patente: {list_principal[4][i]}")
        print(f"Año: {list_principal[5][i]}")
        print(f"Combustible: {list_principal[6][i]}")
        print(f"Puertas: {list_principal[7][i]}")
        print(f"Transmisión: {list_principal[8][i]}")
        print(f"Color: {list_principal[9][i]}")
        print(f"Kilometraje: {list_principal[10][i]}")
        print(f"Precio: {list_principal[11][i]}")
        print("-" * 50)

def modify_car(list_principal):
    print("-" * 50)
    print("\t\tModificar precio/kilometraje")
    print("-" * 50)
    patent = input("Ingrese la patente: ")
    if patent in list_principal[4]:
        index = list_principal[4].index(patent)
        print("1. Modificar precio")
        print("2. Modificar kilometraje")
        while True:
            try:
                option = int(input("Ingrese una opción: "))
                if option == 1:
                    price = validation(int, "Ingrese el nuevo precio: ", 0)
                    list_principal[11][index] = price
                    break
                elif option == 2:
                    km = validation(int, "Ingrese el nuevo kilometraje: ", 0)
                    list_principal[10][index] = km
                    break
                else:
                    raise OutOfRange("Ingrese una opción válida")
            except ValueError:
                print("-" * 50)
                print("Error: Ingrese un número entero")
                print("-" * 50)
            except OutOfRange as e:
                print("-" * 50)
                print("Error:", e.message)
                print("-" * 50)
    else:
        print("La patente no existe")

def sell_car(list_principal):
    print("-" * 50)
    print("\t\tVender auto")
    print("-" * 50)
    patent = input("Ingrese la patente: ")
    if patent in list_principal[4]:
        index = list_principal[4].index(patent)
        print("Nombre:", list_principal[0][index])
        print("Rut:", list_principal[1][index])
        print("Teléfono:", list_principal[2][index])
        print("Correo:", list_principal[3][index])
        print("Patente:", list_principal[4][index])
        print("Año:", list_principal[5][index])
        print("Combustible:", list_principal[6][index])
        print("Puertas:", list_principal[7][index])
        print("Transmisión:", list_principal[8][index])
        print("Color:", list_principal[9][index])
        print("Kilometraje:", list_principal[10][index])
        print("Precio:", list_principal[11][index])
        print("-" * 50)
        print("¿Desea vender el vehículo?")
        print("1. Sí")
        print("2. No")
        while True:
            try:
                option = int(input("Ingrese una opción: "))
                if option == 1:
                    for i in range(len(list_principal)):
                        del list_principal[i][index]
               
                    break
                elif option == 2:
                    break
                else:
                    raise OutOfRange("Ingrese una opción válida")
            except ValueError:
                print("-" * 50)
                print("Error: Ingrese un número entero")
                print("-" * 50)
            except OutOfRange as e:
                print("-" * 50)
                print("Error:", e.message)
                print("-" * 50)
    else:
        print("La patente no existe")