#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified = my_list.copy()

    for a in range(len(my_list)):
        if my_list[a] == search:
            modified[a] = replace
    return (modified)
