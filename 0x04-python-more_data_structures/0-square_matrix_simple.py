#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Nwsquare = []
    j = 0
    for c in matrix:
        Nwsquare.append([])
        for x in matrix[j]:
            Nwsquare[j].append(x**2)
        j += 1
    return (Nwsquare)
