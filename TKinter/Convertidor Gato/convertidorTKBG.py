import tkinter as tk
import requests
import json
from PIL import Image, ImageTk

operacionSeleccionada = "USD-EUR"

#diccionario con valor de las divisas

divisas = {
    "USD": 1.0,
    "EUR": 0.8329,
    "CLP": 772.9476,
    "JPY": 109.4494
}

#funcion que actualiza las divisas con la api de openexchangerates.org

def actualizacionDivisa(api_key):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = json.loads(response.text)["rates"]
        divisas.update(rates)
    else:
        raise Exception("Error al obtener las tasas de cambio")
    
actualizacionDivisa("fc62c57578864e4da8863911995bc617")

#creacion ventana principal

ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Convertidor epico 3: Ahora es personal")

canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()

imagenFondo = Image.open('C:/Users/Sumir/Documents/gato.png')
imagenFondo = ImageTk.PhotoImage(imagenFondo)

canvas.create_image(0, 160, anchor='nw', image=imagenFondo)



#funcion con los calculos

def convertir(divisaOrigen, divisaDestino):
    valorOrigen = float(entradaDivisa.get())
    tasaConversion = eval(f"divisas['{divisaDestino}'] / divisas['{divisaOrigen}']")
    valorDestino = round((valorOrigen * tasaConversion), 2)
    textoResultado.config(text=f"{valorDestino} {divisaDestino}")
    

#menu desplegable con la divisa de origen

operacionesOrigen = ["USD", "EUR", "CLP", "JPY"]
opcionOrigen = tk.StringVar(ventana)
opcionOrigen.set(operacionesOrigen[0])

origen = tk.Label(ventana, text="Origen")
origen.pack()
origen.place(x=170, y=60)

marcoOrigen = tk.Frame(ventana)
marcoOrigen.place(x=170, y=80)

origen = tk.OptionMenu(marcoOrigen, opcionOrigen, *operacionesOrigen)
origen.pack()

#menu con la divisa de destino

operacionesDestino = ["USD", "EUR", "CLP", "JPY"]
opcionDestino = tk.StringVar(ventana)
opcionDestino.set(operacionesDestino[0])

destino = tk.Label(ventana, text="Destino")
destino.pack()
destino.place(x=170, y=120)

marcoDestino = tk.Frame(ventana)
marcoDestino.place(x=170, y=140)

menuDestino = tk.OptionMenu(marcoDestino, opcionDestino, *operacionesDestino)
menuDestino.pack()

#entrada de la cantidad a convertir con un texto arriba
textoCantidad = tk.Label(ventana, text="Cantidad a convertir")
textoCantidad.pack()
textoCantidad.place(x=30, y=80)

entradaDivisa = tk.Entry(ventana)
entradaDivisa.pack()
entradaDivisa.place(x=30, y=100)

#titulo dentro de la ventana

titulo = tk.Label(text="Bienvenid@ al convertidor\nepico de Anette")
titulo.pack()
titulo.place(x=50, y=10)

#texto que muestra el resultado, se actualiza despues


textoResultado = tk.Label(ventana, text="")
textoResultado.pack()
textoResultado.place(x=30, y=120)


def imagen():
    global imagenFondo
    nuevaImagen = Image.open('C:/Users/Sumir/Documents/gato2.png')
    imagenFondo = ImageTk.PhotoImage(nuevaImagen)
    canvas.create_image(0, 140, anchor='nw', image=imagenFondo)

#boton para cambiar, la funcion del boton se cambia con la funcion de mas abajo

boton = tk.Button(ventana, text="Cambiar")
boton.pack()
boton.place(x=100, y=200)

def cambiarFuncion(*args):
    divisaOrigen = opcionOrigen.get()
    divisaDestino = opcionDestino.get()
    boton.config(command=lambda: (convertir(divisaOrigen, divisaDestino), imagen()))

    

opcionOrigen.trace("w", cambiarFuncion)
opcionDestino.trace("w", cambiarFuncion)

#loop principal de la ventana, permite que se ejcute

ventana.mainloop()
