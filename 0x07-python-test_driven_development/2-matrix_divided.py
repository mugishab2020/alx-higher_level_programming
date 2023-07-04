#!/usr/bin/python3
""" This is the function for deviding the matrix"""


def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
    rraise a TypeError exception with the message div must be a number
    Returns a new matrix
    """
    result = []
    if not matrix or matrix is None or matrix is [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int or type(div) is not float or div is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for a in range(len(matrix)):
        if len(matrix[a]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        result.append([])
        for b in range(matrix[a]):
            if type(b) in int or type(b) is float:
                result[a].append(round(b / div, 2))
            else:

                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return result
