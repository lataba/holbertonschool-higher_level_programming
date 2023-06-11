#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""

    new_dictionary = {}

    for key in a_dictionary:
        value = a_dictionary[key]
        new_dictionary[key] = value * 2

    return (new_dictionary)
