#!/usr/bin/python3
""" Thiis function check if the object is for the class 
or for the super classs/ parent class we inherited from
"""
def is_kind_of_class(obj, a_class):
    """ this is the inner part of the function"""
    if isinstance(obj, a_class):
        return True
    return False
