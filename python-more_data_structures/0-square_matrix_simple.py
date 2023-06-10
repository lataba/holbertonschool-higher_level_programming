#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    result = []

    for row in matrix:
        new_row = []

        for i in row:
            new_element = i*i
            new_row.append(new_element)
        result.append(new_row)
           
    return (result)
