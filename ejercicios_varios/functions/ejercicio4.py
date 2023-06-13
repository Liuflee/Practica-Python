import functions as fn

column = fn.validation(int, "Ingrese el numero de columnas: ", 1, 10)
row = fn.validation(int, "Ingrese el numero de filas: ", 1, 10)

column1 = fn.validation(int, "Ingrese el numero de columnas: ", 1, 10)
row1 = fn.validation(int, "Ingrese el numero de filas: ", 1, 10)

array1 = fn.create_array(column, row)
print(array1)
array2 = fn.create_array(column1, row1)
print(array2)

print(fn.create_second_array(array1, array2))