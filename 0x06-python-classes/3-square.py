#!/usr/bin/python3
"""this is the definition of clas Square"""


class Square:
    """
    This is the square class and its private attributes
    It is now defined how square is found
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
