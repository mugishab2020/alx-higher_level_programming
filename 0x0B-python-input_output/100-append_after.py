#!/usr/bin/python3

"""Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """
     a function that inserts a line of text to a file,
    """
    with open(filename, "r") as file_1:
        text = file_1.readlines()

    with open(filename, "w") as file_2:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
        file_2.write(string)
