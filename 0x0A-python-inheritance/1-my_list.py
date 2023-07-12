#!/usr/bin/python3
""" this is the inherited class or child class"""


class MyList(list):
    """ this is the inner of the child class and is sorted"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
