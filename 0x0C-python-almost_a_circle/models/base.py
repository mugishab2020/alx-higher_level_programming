#!/usr/bin/python3
""" this is the first class for this project based on
python overall modeles
Wwe are lookin for importing and many things about pythn and oop
"""
import json
import csv
import turtle


class Base:
    """ this is the base class that we are gonna use in
    this overall project about python
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for ID of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
