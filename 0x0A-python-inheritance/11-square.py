#!/usr/bin/python3
"""defining the subclass of the REctangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class from Rectangle"""

    def __init__(self, size):
        """
        class constructor
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
