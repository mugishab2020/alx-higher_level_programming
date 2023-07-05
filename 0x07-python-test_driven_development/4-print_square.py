#!/usr/bin/python3
""" this is the function the prints the sqared size of #"""


def print_square(size):
    """
    size is the size length of the square
    size must be an integer
    TypeError exception with the message size must be an integer
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
