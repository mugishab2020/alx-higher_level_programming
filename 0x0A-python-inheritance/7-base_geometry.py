#!/usr/bin/python3
"""base geometry class BaseGeometry """


class BaseGeometry:
    """The body of the class BaseGeometry"""

    def area(self):
        """Body of the function Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This is the body of the function to check the value of the name"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
