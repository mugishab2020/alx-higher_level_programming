#!/usr/bin/python3
"""this is the function for appending to the file"""


def append_write(filename="", text=""):
    """we have filename and text to be eppended at the end of the file"""
    with open(filename, 'a') as file:
        return file.write(text)
