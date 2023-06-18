import numpy as np
import random as rd

class OutOfRange(Exception):
    def __init__(self, msg):
        self.msg = msg

def validation(data_type, msg, min_value=0, max_value=10e20):
    while True:
        try:
            amount = data_type(input(msg))
            if (min_value < amount < max_value):
                break
            else:
                raise OutOfRange(f"Ingrese un numero mayor a {min_value} y menor a {max_value}")
        except ValueError:
            print(f"Error: Ingrese un número {data_type.__name__}")
        except OutOfRange as e:
                print("Error:", e.msg)
    return amount

def create_array(rows, columns):
    array = np.array([[round((validation(float, "Ingrese un numero real: ", min_value=float('-inf'))), 2)  for i in range(rows)] for j in range(columns)])
    return array

def mean_by_column(array):
    print("-" * 60)
    column_mean = np.mean(array, axis=0)
    for i in range(len(column_mean)):
        print(F"Promedio de la columna numero {i + 1}: {column_mean[i]:.2f}")
    print("-" * 60)

def sum_by_row(array):
    print("-" * 60)
    row_sum = np.sum(array, axis=1)
    for i in range(len(row_sum)):
        print(F"Suma de la fila numero {i + 1}: {row_sum[i]:.2f}")
    print("-" * 60)

print("-" * 60)