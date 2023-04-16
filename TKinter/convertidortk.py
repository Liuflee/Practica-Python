
#Importar bibliotecas y funciones, tkinter - interfaz, random, imagetk para el bg, messagebox para el mensaje de error
import tkinter as tk
import tkinter.messagebox as mbox
import requests
import json

operacion_seleccionada = "USD-EUR"

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.8329,
    "CLP": 772.9476,
    "JPY": 109.4494
}

def actualizacion_divisa(api_key):
    url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = json.loads(response.text)["rates"]
        exchange_rates.update(rates)
    else:
        raise Exception("Error al obtener las tasas de cambio")
    
actualizacion_divisa("fc62c57578864e4da8863911995bc617")

ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Convertidor epico 3: Ahora es personal")

def convertir(divisa_origen, divisa_destino):
    valor_origen = float(num1.get())
    tasa_conversion = eval(f"exchange_rates['{divisa_destino}'] / exchange_rates['{divisa_origen}']")
    valor_destino = round((valor_origen * tasa_conversion), 2)
    texto.config(text=f"{valor_destino} {divisa_destino}")

marco1 = tk.Frame(ventana)
marco1.place(x=170, y=80)

operaciones = ["USD", "EUR", "CLP", "JPY"]
opcion_seleccionada = tk.StringVar(ventana)
opcion_seleccionada.set(operaciones[0])

menu = tk.OptionMenu(marco1, opcion_seleccionada, *operaciones)
menu.pack()

texto3 = tk.Label(ventana, text="Origen")
texto3.pack()
texto3.place(x=170, y=60)

texto4 = tk.Label(ventana, text="Destino")
texto4.pack()
texto4.place(x=170, y=120)

marco4 = tk.Frame(ventana)
marco4.place(x=170, y=140)

operaciones2 = ["USD", "EUR", "CLP", "JPY"]
opcion_seleccionada2 = tk.StringVar(ventana)
opcion_seleccionada2.set(operaciones2[0])

menu2 = tk.OptionMenu(marco4, opcion_seleccionada2, *operaciones2)
menu2.pack()

texto2 = tk.Label(ventana, text="Cantidad a convertir")
texto2.pack()
texto2.place(x=30, y=80)

num1 = tk.Entry(ventana)
num1.pack()
num1.place(x=30, y=100)

titulo =tk.Label(text="Bienvenid@ al convertidor\nepico de Anette")
titulo.pack()
titulo.place(x=50, y=10)

texto = tk.Label(ventana, text="")
texto.pack()
texto.place(x=30, y=120)

boton = tk.Button(ventana, text="Cambiar")
boton.pack()
boton.place(x=100, y=200)

def cambiar_funcion(*args):
    divisa_origen = opcion_seleccionada.get()
    divisa_destino = opcion_seleccionada2.get()
    boton.config(command=lambda: convertir(divisa_origen, divisa_destino))

opcion_seleccionada.trace("w", cambiar_funcion)
opcion_seleccionada2.trace("w", cambiar_funcion)

ventana.mainloop()
