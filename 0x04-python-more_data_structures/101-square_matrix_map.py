#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda elx: list(map(lambda ely: ely**2, elx)), matrix)))
