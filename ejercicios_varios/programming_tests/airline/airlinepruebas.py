import numpy as np

def print_seats(seats):

    for i, row in enumerate(seats):    
        for seat in row:
            if seat == 0:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print()

seats = np.zeros((33, 6), dtype=int)

print_seats(seats)
