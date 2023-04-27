import random

palabras = {
    "queso": {
        90: "La palabra es un alimento",
        40: "El alimento es de color amarillo",
        10: "El alimento se derrite"
    },
    "dragon": {
        90: "La palabra es un animal mitologico",
        40: "El animal tiene alas",
        10: "El animal suele exhalar fuego"
    },
    "pescado": {
        90: "La palabra es un animal acuatico",
        40: "El animal puede nadar",
        10: "El animal tiene branquias"
    },
    "gato": {
        90: "La palabra es un animal terrestre",
        40: "El animal tiene 4 patas",
        10: "El animal es domestico"
    },
    "taza": {
        90: "La palabra es un utensilio de cocina",
        40: "El utensilio está relacionado al café",
        10: "El utensilio sirve para beber liquidos"
    },
    "audifonos": {
        90: "La palabra es un objeto electronico",
        40: "El objeto tiene relación con la musica",
        10: "El objeto está asociado a las orejas"
    }
}

eleccion = random.choice(list(palabras.keys()))
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
        else:
            puntuacion = puntuacion - 10
            if puntuacion in palabras[eleccion]:
                print(palabras[eleccion][puntuacion])

            if puntuacion == 0:
                print("Perdiste, tu puntuación llegó a 0")
                break
