#!usr/bin/python3
"""This is function of adding two numbers """


def add_integer(a, b=98):
    """
    a and b must be integers or floats
    otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    """
    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return a + b
        else:
            raise TypeError("a must be an integer or b must be an integer")
    else:
        raise TypeError("a must be an integer or b must be an integer")
