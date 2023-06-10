#!/usr/bin/python3

def common_elements(set_1, set_2):
    """function that returns a set of common elements in two sets"""

    resu_set = set()

    for elem1 in set_1:
        for elem2 in set_2:
            if elem1 == elem2:
                resu_set.add(elem2)

    return (resu_set)
