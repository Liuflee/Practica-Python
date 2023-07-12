import functions as fn

opciones = [
    "Comprar Entradas",
    "Mostrar ubicaciones",
    "Ver Asistentes",
    "Mostrar ganancias",
    "Salir"
]

asientos = fn.crear_array()
rut = fn.crear_array()

while True:
    opc = fn.menu(opciones)
    if opc == 1:
        fn.comprar_entradas(asientos, rut)
    elif opc == 2:
        fn.imprimir_array(asientos)
    elif opc == 3:
        fn.mostrar_asistentes(rut)
    elif opc == 4:
        fn.mostrar_ganancias(asientos)
    else:
        break