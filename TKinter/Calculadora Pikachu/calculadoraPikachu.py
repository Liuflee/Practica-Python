
#Importar bibliotecas y funciones, tkinter - interfaz, random, imagetk para el bg, messagebox para el mensaje de error
import tkinter as tk
import random
from PIL import Image, ImageTk
import tkinter.messagebox as mbox

#Creación ventana principal de tk
ventana = tk.Tk()
ventana.geometry("250x250")

#Random entre 1 y 6

azar = random.randint(1, 6)

#Titulos aleatorios para la ventana segun la funcion de arriba

if azar == 1:
    ventana.title("Epic Calculator")
elif azar==2:
    ventana.title("Epic Calculator 2: Ahora es personal")
elif azar==4:
    ventana.title("Epic Calculator: Ahora con menos bugs")
elif azar==5:
    ventana.title("Epic Calculator: ¡Prueba el té de burbujas!")
else:
    ventana.title("Eso Tilin")

#canvas para el bg de pikachu
canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()

imagen_fondo = Image.open('C:/Users/Sumir/Documents/XoQ2Mx0.png')
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

canvas.create_image(0, 0, anchor='nw', image=imagen_fondo)


#definicion de las funciones para las operaciones matematicas

def suma():
    resultado = float(num1.get()) + float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def resta():
    resultado = float(num1.get()) - float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def division():
    resultado = float(num1.get()) / float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def multiplicación():
    resultado = float(num1.get()) * float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

#La funcion de potencia tiene un mensaje de error si el resultado es demasiado grande

def potencia():
    try:
        resultado = float(num1.get()) ** float(num2.get())
        if abs(resultado) > 1e12:
            raise ValueError("Resultado demasiado grande para mostrar")
        texto.config(text=f"El resultado es {resultado}")
    except Exception as e:
        texto.config(text="")
        mbox.showerror("Error", "Resultado demasiado grande para mostrar")


#menú desplegable con las opciones de operación
marco1 = tk.Frame(ventana)
marco1.place(x=170, y=100)

operaciones = ["Suma", "Resta", "División", "Multiplicación", "Potencia"]
opcion_seleccionada = tk.StringVar(ventana)
opcion_seleccionada.set(operaciones[0])

menu = tk.OptionMenu(marco1, opcion_seleccionada, *operaciones)
menu.pack()

#entradas para los numeros en la ventana

num1 = tk.Entry(ventana)
num1.pack()
num1.place(x=30, y=100)

num2 = tk.Entry(ventana)
num2.pack()
num2.place(x=30, y=120)

#titulo dentro de la ventana

titulo =tk.Label(text="Bienvenid@ a la calculadora\nepica de Anette")
titulo.pack()
titulo.place(x=50, y=30)

#texto que da la operación, vacio por ahora

texto = tk.Label(ventana, text="")
texto.pack()
texto.place(x=70, y=150)

#boton para calcular

boton = tk.Button(ventana, text="Calcular")
boton.pack()
boton.place(x=100, y=180)
boton.config(command=suma)

#funcion que cambia lo que hace el boton segun lo seleccionado en el menú

def cambiar_funcion(*args):
    if opcion_seleccionada.get() == "Suma":
        boton.config(command=suma)
    elif opcion_seleccionada.get() == "Resta":
        boton.config(command=resta)
    elif opcion_seleccionada.get() == "División":
        boton.config(command=division)
    elif opcion_seleccionada.get() == "Multiplicación":
        boton.config(command=multiplicación)
    elif opcion_seleccionada.get() == "Potencia":
        boton.config(command=potencia)

opcion_seleccionada.trace("w", cambiar_funcion)


#loop principal que ejcuta la ventana

ventana.mainloop()
