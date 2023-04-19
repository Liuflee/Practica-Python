import random

palabras = ("queso", "dragon", "pescado", "gato", "taza", "audifonos",)
eleccion = random.choice(palabras)
elecPlayer = 0
puntuacion = 100

while True:
    try:
        elecPlayer = input("Trata de adivinar la palabra: ").lower()
        if not elecPlayer.isalpha():
            raise TypeError("Debes ingresar una palabra")        
    except TypeError as error:
        print(f"Error: {error}")
    else:
        if elecPlayer == eleccion:
            print(f"Ganaste, la palabra correcta era {eleccion} y tu puntuación es: {puntuacion}")
            break
        elif eleccion == palabras[0]:
             print("Pista: La palabra es un alimento")
             puntuacion = puntuacion - 10
        elif eleccion == palabras[1]:
            print("Pista: La palabra es un animal mitológico")
            puntuacion = puntuacion - 10
        elif eleccion == palabras[2]:
            print("Pista: La palabra es un animal acuático")
            puntuacion = puntuacion - 10
        elif eleccion == palabras[3]:
            print("Pista: La palabra es un animal terrestre")
            puntuacion = puntuacion - 10
        elif eleccion == palabras[4]:
            print("Pista: La palabra está relacionada al café")
            puntuacion = puntuacion - 10
        elif eleccion == palabras[5]:
            print("Pista: La palabra está relacionada a la música")
            puntuacion = puntuacion - 10

        if puntuacion == 0:
            print("Perdiste, tu puntuación llegó a 0")
            break
