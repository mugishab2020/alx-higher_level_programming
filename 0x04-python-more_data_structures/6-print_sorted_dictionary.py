#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = list(a_dictionary.keys())
    sorted_keys.sort()
    for keys in sorted_keys:
        print("{}: {}".format(keys, a_dictionary.get(keys)))
