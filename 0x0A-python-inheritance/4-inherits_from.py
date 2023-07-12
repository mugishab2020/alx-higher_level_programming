#!/usr/bin/python3
""" this function checks if the object is from the parent class"""


def inherits_from(obj, a_class):
    """ this is the body of the function"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
