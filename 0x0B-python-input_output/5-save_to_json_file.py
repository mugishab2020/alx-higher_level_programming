#!/usr/bin/python3
"""Json wahala"""
import json
""" this is the file to save oto json file"""


def save_to_json_file(my_obj, filename):
    """
    function for saving to the json file
    """
    with open(filename, 'w') as myFile:
        return json.dump(my_obj, myFile)
