import tkinter as tk
from tkinter import messagebox
import urllib.request
import requests
import json
import time
from PIL import Image, ImageTk

'''Diccionario con valor de las divisas'''
divisas = {
    "USD": 1.0,
    "EUR": 0.8329,
    "CLP": 772.9476,
    "JPY": 109.4494,
    "ARS": 217.439,
    "MXN": 18.092843
}

'''URL con las imagenes de los gatos'''
url = "https://i.imgur.com/iNqMjGS.png"
gato, headers = urllib.request.urlretrieve(url)
url2 = "https://i.imgur.com/xZJ38rX.png"
gato2, headers2 = urllib.request.urlretrieve(url2)

def actualizacionDivisa(api_key):
    """Actualiza las tasas de cambio con la API de openexchangerates.org"""
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = json.loads(response.text)["rates"]
        divisas.update(rates)
    else:
        raise Exception("Error al obtener las tasas de cambio")
    
actualizacionDivisa("fc62c57578864e4da8863911995bc617")

def convertir(divisaOrigen, divisaDestino):
    """Convierte una cantidad de una divisa a otra"""
    try:
        valorOrigen = float(entradaDivisa.get())
        tasaConversion = eval(f"divisas['{divisaDestino}'] / divisas['{divisaOrigen}']")
        valorDestino = round((valorOrigen * tasaConversion), 2)
        textoResultado.config(text=f"{valorDestino} {divisaDestino}")
    except ValueError:
         messagebox.showerror("Error", "La cantidad ingresada no es un número válido") 

def imprimirTexto(texto, widget, velocidad):
    '''Funcion que imprime el texto progresivamente'''
    for i in range(len(texto)):
        widget.config(text=texto[:i+1])
        widget.update()
        time.sleep(velocidad)

def imagen():
    '''Cambia la imagen'''
    global imagenFondo
    nuevaImagen = Image.open(gato2)
    imagenFondo = ImageTk.PhotoImage(nuevaImagen)
    canvas.create_image(0, 140, anchor='nw', image=imagenFondo)

def cambiarFuncion(*args):
    """Cambia la función del botón para incluir la conversión de divisas
    y la actualización de la imagen"""
    divisaOrigen = opcionOrigen.get()
    divisaDestino = opcionDestino.get()
    boton.config(command=lambda: (convertir(divisaOrigen, divisaDestino), imagen()))

'''Creación de la ventana principal con su titulo'''
ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Convertidor epico 3: Ahora es personal")

'''Imagen del gato1'''
canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()

imagenFondo = Image.open(gato)
imagenFondo = ImageTk.PhotoImage(imagenFondo, format="PNG")
canvas.create_image(0, 160, anchor='nw', image=imagenFondo)

'''Menú desplegable con la divisa de origen'''
operacionesOrigen = ["USD", "EUR", "CLP", "JPY", "ARS", "MXN"]
opcionOrigen = tk.StringVar(ventana)
opcionOrigen.set(operacionesOrigen[0])

marcoOrigen = tk.Frame(ventana)
marcoOrigen.place(x=170, y=80)

menuOrigen = tk.OptionMenu(marcoOrigen, opcionOrigen, *operacionesOrigen)
menuOrigen.pack()

'''Menú desplegable con la divisa de destino'''
operacionesDestino = ["USD", "EUR", "CLP", "JPY", "ARS", "MXN"]
opcionDestino = tk.StringVar(ventana)
opcionDestino.set(operacionesDestino[0])

marcoDestino = tk.Frame(ventana)
marcoDestino.place(x=170, y=140)

menuDestino = tk.OptionMenu(marcoDestino, opcionDestino, *operacionesDestino)
menuDestino.pack()

'''Label con un titulo dentro de la ventana'''
titulo = tk.Label()
titulo.pack()
titulo.place(x=50, y=10)
textoImpresion = "Bienvenid@ al convertidor\n epico de Anette"

'''Label que muestra el resultado, se actualiza despues con la 
funcion convertir()dentro de cambiarFuncion()'''
textoResultado = tk.Label(ventana)
textoResultado.pack()
textoResultado.place(x=30, y=120)

'''Label ubicado arriba del menú de origen'''
origen = tk.Label(ventana)
origen.pack()
origen.place(x=170, y=60)
textoOrigen = "Origen"

'''Label ubicado arriba del menú de destino'''
destino = tk.Label(ventana)
destino.pack()
destino.place(x=170, y=120)
textoDestino = "Destino"

'''Label ubicado arriba de la entrada de los numeros'''
labelCantidad = tk.Label(ventana)
labelCantidad.pack()
labelCantidad.place(x=30, y=80)
textoCantidad = "Cantidad a convertir"

'''Entrada de los numeros'''
entradaDivisa = tk.Entry(ventana)
entradaDivisa.pack()
entradaDivisa.place(x=30, y=100)

'''Se llama a la función imprimirTexto() para escribir
todo el texto de la ventana progresivamente'''
imprimirTexto(textoImpresion, titulo, 0.01)
imprimirTexto(textoCantidad, labelCantidad, 0.03)
imprimirTexto(textoOrigen, origen, 0.03)
imprimirTexto(textoDestino, destino, 0.03)

'''Creación del boton'''
boton = tk.Button(ventana, text="Cambiar")
boton.pack()
boton.place(x=100, y=200)


'''Cambia la función del botón segun que se elija en los menús desplegable'''
opcionOrigen.trace("w", cambiarFuncion)
opcionDestino.trace("w", cambiarFuncion)

'''Loop principal de la ventana, permite que se ejecute'''
ventana.mainloop()
