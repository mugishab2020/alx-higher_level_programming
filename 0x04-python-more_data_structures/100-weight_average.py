#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    integer = 0
    den = 0

    for tupple in my_list:
        integer += tupple[0] * tupple[1]
        den += tupple[1]

    return (integer / den)
