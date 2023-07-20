#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ property def of seize"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def to_dictionary(self):
        """eturns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
