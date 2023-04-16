import tkinter as tk
import requests
import json
from PIL import Image, ImageTk
import time
import os
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

# Obtener el directorio actual del archivo principal
dir_actual = os.path.dirname(os.path.abspath(__file__))

# Unir la ruta del directorio actual con la carpeta "img" y el nombre de la imagen
ruta_imagen = os.path.join(dir_actual, 'img', 'gato.png')

imagen_fondo = Image.open(ruta_imagen)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

canvas.create_image(0, 160, anchor='nw', image=imagen_fondo_tk)

#funcion con los calculos

def convertir(divisaOrigen, divisaDestino):
    valorOrigen = float(entradaDivisa.get())
    tasaConversion = eval(f"divisas['{divisaDestino}'] / divisas['{divisaOrigen}']")
    valorDestino = round((valorOrigen * tasaConversion), 2)
    textoResultado.config(text=f"{valorDestino} {divisaDestino}")
    
def imprimirTexto(texto, widget):
    for i in range(len(texto)):
        widget.config(text=texto[:i+1])
        widget.update()
        time.sleep(0.035)

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

titulo = tk.Label()
titulo.pack()
titulo.place(x=50, y=10)

textoImpresion = "Bienvenid@ al convertidor\n epico de Anette"
imprimirTexto(textoImpresion, titulo)
#texto que muestra el resultado, se actualiza despues

textoResultado = tk.Label(ventana)
textoResultado.pack()
textoResultado.place(x=30, y=120)

boton = tk.Button(ventana, text="Cambiar")

def cambiarFuncion(*args):
    global imagen_fondo_tk
    divisaOrigen = opcionOrigen.get()
    divisaDestino = opcionDestino.get()
    imagen_fondo_tk = imagen_fondo_tk
    boton.config(command=lambda: (convertir(divisaOrigen, divisaDestino), imagen()))
    
boton.pack()
boton.place(x=100, y=200)

# Definir la función para cambiar la imagen de fondo
def imagen():
    global imagen_fondo_tk
    ruta_nueva_imagen = os.path.join(dir_actual, 'img', 'gato2.png')
    nueva_imagen = Image.open(ruta_nueva_imagen)
    imagen_fondo_tk = ImageTk.PhotoImage(nueva_imagen)
    canvas.create_image(0, 140, anchor='nw', image=imagen_fondo_tk)

opcionOrigen.trace("w", cambiarFuncion)
opcionDestino.trace("w", cambiarFuncion)

#loop principal de la ventana, permite que se ejcute

ventana.mainloop()
