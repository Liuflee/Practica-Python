import math

def main():
    # Utilizar nombres descriptivos para variables y funciones
    mensaje_saludo = obtener_saludo()
    imprimir_mensaje(mensaje_saludo)

    # Utilizar funciones para tareas repetitivas
    numeros = [1, 2, 3, 4, 5]
    numeros_pares = filtrar_pares(numeros)
    imprimir_numeros(numeros_pares)

    # Utilizar comentarios para explicar el código
    # Este bucle imprime los números pares de la lista

    # Utilizar tipos de datos seguros y anotaciones de tipo
    nombre = "Juan"
    edad: int = 25

    # Evitar la duplicación de código
    resultado = sumar(2, 3)
    imprimir_mensaje(f"El resultado de la suma es {resultado}")

def obtener_saludo() -> str:
    return "Hola, bienvenido!"

def filtrar_pares(numeros: list) -> list:
    return [num for num in numeros if num % 2 == 0]

def imprimir_mensaje(mensaje: str):
    print(mensaje)

def imprimir_numeros(numeros: list):
    for num in numeros:
        print(num)

def sumar(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    main()

