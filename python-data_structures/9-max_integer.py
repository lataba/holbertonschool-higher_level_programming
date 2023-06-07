#!/usr/bin/python3

def max_integer(my_list=[]):

    if my_list:

        aux = my_list[0]

        for num in my_list:
            if num > aux:
                aux = num
        return (aux)

    return (None)
