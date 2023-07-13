#!/usr/bin/python3
""" JSON wahala"""
import json
"""this is hete to Create object from a JSON file
"""


def load_from_json_file(filename):
    """ function to create object from a JSON file"""
    with open(filename) as myFile:
        return json.load(myFile)
