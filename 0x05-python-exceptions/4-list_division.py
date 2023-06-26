#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    devid = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                result = element_1 / element_2
                devid.append(result)
            except ZeroDivisionError:
                print("division by 0")
                devid.append(0)
            except TypeError:
                print("wrong type")
                devid.append(0)
            except IndexError:
                print("out of range")
                devid.append(0)
    finally:
        return devid
