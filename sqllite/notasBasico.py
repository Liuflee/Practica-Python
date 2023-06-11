import sqlite3

conexion = sqlite3.connect("dataNotasBasico.db")

cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS notas
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                contenido TEXT);''')

titulo = input('Nombre de la nota: ')
contenido = input('Contenido: ')

queryinput = """
INSERT INTO notas (titulo, contenido)
VALUES (?, ?);
"""
cursor.execute(queryinput, (titulo, contenido))

conexion.commit()

cursor.execute('SELECT * FROM notas;')

print('\nNotas:')

for columna in cursor.fetchall():
    nombreDisplay = columna[1]
    descripcionDisplay = columna[2]

    print("*" * 50)
    print(f'Nombre de la nota: {nombreDisplay}\nContenido: {descripcionDisplay}\n')


cursor.close()

conexion.close()