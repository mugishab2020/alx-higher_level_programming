#!/usr/bin/python3

"""Pascal's Triangle"""


def pascal_triangle(n):
    """list of lists of integers representing the Pascal’s triangle
    """
    tr = []
    if n <= 0:
        return tr
    if n == 0:
        return [[1]]

    tr = [[1]]
    for i in range(n-1):
        tr.append([a+b for a, b in zip([0] + tr[-1], tr[-1] + [0])])
    return tr
