#!/usr/bin/python3
"""class"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__

        else:
            a = {}
            for attr in attrs:
                if hasattr(self, attr):
                    a[attr] = getattr(self, attr)
            return a

    def reload_from_json(self, json):
        """ replaces all attributes of Student instance"""
        for keys in json:
            setattr(self, keys, json[keys])
