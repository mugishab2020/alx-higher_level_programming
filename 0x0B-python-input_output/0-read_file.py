#!/usr/bin/python3
"""This is the begginign of the file open and use projeect
we are gonna deal with the file
"""


def read_file(filename=""):
    """This is the first function we are creating and is for
    file opening and read
    """
    with open(filename) as file:
        content = file.read()
    print(content, end="")
