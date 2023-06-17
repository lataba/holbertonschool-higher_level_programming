#!/usr/bin/python3
"""
In this module: a function that prints a text line is defined
"""


def say_my_name(first_name, last_name=""):
    """
    Definition of the function that prints My name is <first name> <last name>
    Raises:
        TypeError: If last_name or first_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name == "":
        print("My name is {}".format(last_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
