#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        i = 0
        for element in row:
            i = i + 1
            if i < len(row):
                print("{:d}".format(element), end=' ')
            else:
                print("{}".format(element))
        if i == 0:
            print('')
