import sqlite3
import tkinter as tk


ventana = tk.Tk()
ventana.geometry("550x500")
ventana.title("Notas")


titulo = tk.Label(ventana, text="Título:")
titulo.grid(row=0, column=0, padx=10, pady=10)

entrada_titulo = tk.Entry(ventana, width=50)
entrada_titulo.grid(row=0, column=1, padx=10, pady=10)

contenido = tk.Label(ventana, text="Contenido:")
contenido.grid(row=1, column=0, padx=10, pady=10)

entrada_contenido = tk.Text(ventana, width=50, height=10)
entrada_contenido.grid(row=1, column=1, padx=10, pady=10)

boton_guardar = tk.Button(ventana, text="Guardar", command=lambda: guardar())
boton_guardar.grid(row=2, column=0, padx=10, pady=10)

boton_borrar_todo = tk.Button(ventana, text="Borrar todo", command=lambda: borrar_todo())
boton_borrar_todo.grid(row=2, column=1, padx=10, pady=10)

texto = tk.Label(ventana, text="")
texto.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


def guardar():
    titulo = entrada_titulo.get()
    contenido = entrada_contenido.get("1.0", tk.END)
   
    conexion = sqlite3.connect("dataNotas.db")
    cursor = conexion.cursor()
    queryinput = "INSERT INTO notas (titulo, contenido) VALUES (?, ?)"
    cursor.execute(queryinput, (titulo, contenido))
    conexion.commit()
    

    cambiar_texto()

def borrar_todo():
 
    conexion = sqlite3.connect("dataNotas.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM notas")
    conexion.commit()
    

    cambiar_texto()

def cambiar_texto():

    conexion = sqlite3.connect("dataNotas.db")
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM notas;')

    texto_notas = ""
    for columna in cursor.fetchall():
        nombre_display = columna[1]
        descripcion_display = columna[2]

        texto_notas += f"Titulo: {nombre_display}\n{descripcion_display}\n\n"

    texto.config(text=texto_notas)

    cursor.close()
    conexion.close()


conexion = sqlite3.connect("dataNotas.db")
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS notas
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                contenido TEXT);''')

cambiar_texto()


ventana.mainloop()
