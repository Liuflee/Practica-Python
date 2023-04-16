
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

