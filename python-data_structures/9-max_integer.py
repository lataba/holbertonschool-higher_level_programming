#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list:

        aux = 0

        for num in my_list:
            if num > aux:
                aux = num
        return (aux)

    return (None)
