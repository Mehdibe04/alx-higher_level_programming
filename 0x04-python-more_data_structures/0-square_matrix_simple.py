#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nw_matrix = [list(row) for row in matrix]
    for x in range(len(nw_matrix)):
        for y in range(len(nw_matrix[i])):
            nw_matrix[x][y] *= nw_matrix[x][y]
    return nw_matrix
