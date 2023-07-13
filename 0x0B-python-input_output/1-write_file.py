#!/usr/bin/python3
"""
This is the function to write some text on the file
"""


def write_file(filename="", text=""):
    """
    This is the inner of te function
    we have filename and the text to be written on the filename
    given """

    with open(filename, 'w') as file:
        return file.write(text)
