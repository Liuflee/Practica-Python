class OutOfRange(Exception):
    def __init__(self, msg):
        self.msg = msg

def validation(data_type, msg, min_v=0, max_v=int('inf')):
    while True:
        try:
            num = data_type(input(msg))
            if not (min_v < num < max_v):
                raise OutOfRange(f"Ingrese un numero mayor a {min_v} y menor a {max_v}")
            else:
                break
        except ValueError:
            print(f"Error: Ingrese un numero {data_type}")
        except OutOfRange as e:
                print("Error:", e.msg)
    return num

def circle_area(radius):
    import math
    area = (math.pi * radius**2)
    print(f"El área del circulo es: {area:.1f}")
    return area

def square_perimeter(side):   
    perimeter = (4 * side)
    print(f"El perimetro del cuadrado es: {perimeter:.1f}")
    return perimeter

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
            print("Error: Ingrese un numero entero")
            print("-" * 50)
        except OutOfRange as e:
            print("-" * 50)
            print("Error:", e)
            print("-" * 50)
    return chosen_option
