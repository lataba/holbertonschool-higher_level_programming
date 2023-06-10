#!/usr/bin/python3

def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list"""

    sum = 0
    my_set = set()

    for i in range(len(my_list)):

        if my_list[i] not in my_set:
            my_set.add(my_list[i])
            sum = sum + my_list[i]
    return (sum)
