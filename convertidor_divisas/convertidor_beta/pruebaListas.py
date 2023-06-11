import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

url = "https://i.imgur.com/iNqMjGS.png"
response = requests.get(url)

ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Convertidor epico 3: Ahora es personal")

canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()

imagenFondo = Image.open(io.BytesIO(response.content))
imagenFondo = ImageTk.PhotoImage(imagenFondo, format="PNG")
canvas.create_image(0, 160, anchor='nw', image=imagenFondo)

ventana.mainloop()
