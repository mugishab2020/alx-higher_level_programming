#!/usr/bin/python3
""" stiident clas creation"""


class Student:
    """the class initiation """
    def __init__(self, first_name, last_name, age):
        """ this is the constructor of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionaty retrivial"""
        return self.__dict__
