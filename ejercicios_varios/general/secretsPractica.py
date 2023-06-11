import secrets
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import urllib.request

def cambiar():
    password = secrets.token_hex(4)
    textoPass.config(text=f"La contraseña es {password}")

url = "https://i.imgur.com/iNqMjGS.png"
gato, headers = urllib.request.urlretrieve(url) 

ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Generador de contraseñas")

imagenFondo = Image.open(gato)
imagenFondo = ImageTk.PhotoImage(imagenFondo, format="PNG")
canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()
canvas.create_image(0, 160, anchor='nw', image=imagenFondo)


style = ttk.Style()
style.configure('W.TButton', borderwidth=0, bordercolor='black', 
                foreground='Black', background='blue', 
                focuscolor='none', focusthickness=0, 
                relief='flat', anchor='center', 
                font=('Lato', 11, 'normal'),
                hovercolor='red')


boton = ttk.Button(ventana, text='Generar', style='W.TButton', 
                 width=7, padding=6,
                 command=cambiar)

boton.place(x=85, y=160)



texto = tk.Label(ventana, text="Bienvenid@ al generador de\ncontraseñas epico de Anette",
                 font=("Lato", 12, "normal"), anchor="nw")

texto.place(x=20, y=30)

textoPass = tk.Label(ventana, font=("Lato", 10, "normal"))
textoPass.place(x=45, y=130)

ventana.mainloop()

