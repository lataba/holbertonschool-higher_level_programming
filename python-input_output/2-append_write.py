#!/usr/bin/python3
"""
Module that defines a function that appends a string at the end of a file
"""


def append_write(filename="", text=""):
    """Appends string"""
    with open(filename, "a", encoding="UTF8") as file:
        file.write(text)

    return len(text)
