import secrets
import tkinter as tk

def cambiar():
    password = secrets.token_hex(4)
    textoPass.config(text=f"La contraseña es {password}")

ventana = tk.Tk()
ventana.geometry("250x250")
ventana.title("Generador de contraseñas")

texto = tk.Label(ventana, text="Bienvenid@ al generador de\ncontraseñas epico de Anette")
texto.pack()
texto.place(x=50, y=10)

boton = tk.Button(ventana, text="Generar", command=cambiar)
boton.pack()
boton.place(x=100, y=125)
boton.config()

textoPass = tk.Label(ventana)
textoPass.pack()
textoPass.place(x=60, y=100)




ventana.mainloop()


'''
Password = secrets.token_hex(8)  # Genera una contraseña segura de 16 caracteres
print(password)
'''