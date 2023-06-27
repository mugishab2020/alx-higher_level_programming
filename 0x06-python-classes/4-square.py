#!/usr/bin/python3
"""this Squrae clas definition"""


class Square:
    """
    this declaration of class Squre
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        to retrieve the clas
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        function to modify the attributes
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
