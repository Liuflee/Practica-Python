import tkinter as tk, urllib.request, requests, json, time
from PIL import Image, ImageTk
from tkinter import messagebox

#diccionario con valor de las divisas

divisas = {
    "USD": 1.0,
    "EUR": 0.8329,
    "CLP": 772.9476,
    "JPY": 109.4494,
    "ARS": 217.439,
    "MXN": 18.092843
}

'''funcion que actualiza las divisas con la api de openexchangerates.org
se requiere un api key de openexchange'''

def actualizacionDivisa(api_key):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = json.loads(response.text)["rates"]
        divisas.update(rates)
    else:
        raise Exception("Error al obtener las tasas de cambio")

actualizacionDivisa("fc62c57578864e4da8863911995bc617")

#funcion con los calculos

def convertir(divisaOrigen, divisaDestino):
    try:
        valorOrigen = float(entradaDivisa.get())
        tasaConversion = eval(f"divisas['{divisaDestino}'] / divisas['{divisaOrigen}']")
        valorDestino = round((valorOrigen * tasaConversion), 2)
        textoResultado.config(text=f"{valorDestino} {divisaDestino}")
    except ValueError:
         messagebox.showerror("Error", "La cantidad ingresada no es un número válido") 

#funciones que imprimen el texto progresivamente
def imprimirTexto(texto, widget):
    for i in range(len(texto)):
        widget.config(text=texto[:i+1])
        widget.update()
        time.sleep(0.01)

def imprimirTextoPequeño(texto, widget):
    for i in range(len(texto)):
        widget.config(text=texto[:i+1])
        widget.update()
        time.sleep(0.03)

#función que cambia la imagen

def imagen():
    global imagenFondo
    nuevaImagen = Image.open(gato2)
    imagenFondo = ImageTk.PhotoImage(nuevaImagen)
    canvas.create_image(0, 140, anchor='nw', image=imagenFondo)

#función que da el resultado y llama a las demas funciones

def cambiarFuncion(*args):
    divisaOrigen = opcionOrigen.get()
    divisaDestino = opcionDestino.get()
    boton.config(command=lambda: (convertir(divisaOrigen, divisaDestino), imagen()))

#url con las imagenes de los gatos

url = "https://i.imgur.com/iNqMjGS.png"
gato, headers = urllib.request.urlretrieve(url)
url2 = "https://i.imgur.com/xZJ38rX.png"
gato2, headers2 = urllib.request.urlretrieve(url2)

#creacion ventana principal

ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Convertidor epico 3: Ahora es personal")

canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()

#Foto gato 1 bg
imagenFondo = Image.open(gato)
imagenFondo = ImageTk.PhotoImage(imagenFondo, format="PNG")
canvas.create_image(0, 160, anchor='nw', image=imagenFondo)

#menu desplegable con la divisa de origen
operacionesOrigen = ["USD", "EUR", "CLP", "JPY", "ARS", "MXN"]
opcionOrigen = tk.StringVar(ventana)
opcionOrigen.set(operacionesOrigen[0])

marcoOrigen = tk.Frame(ventana)
marcoOrigen.place(x=170, y=80)

menuOrigen = tk.OptionMenu(marcoOrigen, opcionOrigen, *operacionesOrigen)
menuOrigen.pack()

#Texto "Destino"
origen = tk.Label(ventana)
origen.pack()
origen.place(x=170, y=60)
textoOrigen = "Origen"

#menu con la divisa de destino
operacionesDestino = ["USD", "EUR", "CLP", "JPY", "ARS", "MXN"]
opcionDestino = tk.StringVar(ventana)
opcionDestino.set(operacionesDestino[0])

marcoDestino = tk.Frame(ventana)
marcoDestino.place(x=170, y=140)

menuDestino = tk.OptionMenu(marcoDestino, opcionDestino, *operacionesDestino)
menuDestino.pack()

#Texto "Destino"
destino = tk.Label(ventana)
destino.pack()
destino.place(x=170, y=120)
textoDestino = "Destino"

#label con el texto arriba de la entrada

labelCantidad = tk.Label(ventana)
labelCantidad.pack()
labelCantidad.place(x=30, y=80)
textoCantidad = "Cantidad a convertir"

#entrada de la cantidad a convertir con un texto arriba
entradaDivisa = tk.Entry(ventana)
entradaDivisa.pack()
entradaDivisa.place(x=30, y=100)

#titulo dentro de la ventana

titulo = tk.Label()
titulo.pack()
titulo.place(x=50, y=10)
textoImpresion = "Bienvenid@ al convertidor\n epico de Anette"

#Se llama a las funciones para escribir el texto progresivamente

imprimirTexto(textoImpresion, titulo)
imprimirTextoPequeño(textoCantidad, labelCantidad)
imprimirTextoPequeño(textoOrigen, origen)
imprimirTextoPequeño(textoDestino, destino)

#texto que muestra el resultado, se actualiza despues con la funcion convertir() dentro de cambiarFuncion()

textoResultado = tk.Label(ventana)
textoResultado.pack()
textoResultado.place(x=30, y=120)


#boton para cambiar, la funcion del boton se cambia con la funcion cambiarFuncion(), 

boton = tk.Button(ventana, text="Cambiar")
boton.pack()
boton.place(x=100, y=200)

opcionOrigen.trace("w", cambiarFuncion)
opcionDestino.trace("w", cambiarFuncion)

#loop principal de la ventana, permite que se ejcute

ventana.mainloop()
