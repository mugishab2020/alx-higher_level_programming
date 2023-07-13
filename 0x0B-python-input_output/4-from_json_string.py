#!/usr/bin/python3
"""Json wahala"""
import json
"""From JSON string to Object"""


def from_json_string(my_str):
    """ function to  returns an object (Python data structure)
    represented by a JSON string"""
    return json.loads(my_str)
