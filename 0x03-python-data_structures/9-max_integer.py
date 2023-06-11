#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    maximum_num = my_list[0]
    for num in my_list:
        if num > maximum_num:
            maximum_num = num

    return maximum_num
