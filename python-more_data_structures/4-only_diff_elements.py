#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """function that returns a set of all elements present in only one set"""

    diff_set = set()

    for elem1 in set_1:
        if elem1 not in set_2:
            diff_set.add(elem1)

    for elem2 in set_2:
        if elem2 not in set_1:
            diff_set.add(elem2)

    return (diff_set)
