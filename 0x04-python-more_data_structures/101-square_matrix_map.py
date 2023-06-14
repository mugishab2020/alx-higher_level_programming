#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda element_x: list(map(lambda element_y: element_y**2, element_x)), matrix)))
