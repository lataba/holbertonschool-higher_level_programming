#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """function that replaces all occurrences of an element in a list"""

    new_list = my_list[:]
    i = 0

    for elem in new_list:
        i = i + 1
        if elem == search:
            new_list[i] = replace

    return (new_list)
