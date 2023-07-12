#!/usr/bin/python3
""" The class Rectangle inheriting from Geometry nclass"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ body of the class"""
    def __init__(self, width, height):
        """constructor for the class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
