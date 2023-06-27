#!/usr/bin/python3
"""defintion of the Square class"""


class Square:
    """
    Thiss is the ckass Sqaure and its attributes
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Retreaving the attributes"""
        return self.__size

    @size.setter
    def size(self, value):
        """modifying the attributes"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This is for Squaring"""
        return self.__size ** 2

    def my_print(self):
        """"printing the Square we found"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
