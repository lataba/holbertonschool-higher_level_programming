#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists"""
    resu_list = []

    for i in range(0, list_length):

        try:
            resu = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            print("division by 0")
            resu = 0
        except IndexError:
            print("out of range")
            resu = 0
        except TypeError:
            print("wrong type")
            resu = 0
        finally:
            resu_list.append(resu)

    return (resu_list)
