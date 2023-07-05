#!/usr/bin/python3
"""here we got the functioning rectangle"""


class Rectangle:
    """
    here we make the private attributes by using @property
    and we make the other one witout @property
    to indicate that they are publuc attributes
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This is the claculator of area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ Thi sis the calculator of the permeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))
