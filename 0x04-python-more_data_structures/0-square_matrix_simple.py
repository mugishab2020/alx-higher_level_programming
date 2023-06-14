#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = matrix.copy()

    for a in range(len(matrix)):
        squared_matrix[a] = list(map(lambda i: i**2, matrix[a]))

    return (squared_matrix)
