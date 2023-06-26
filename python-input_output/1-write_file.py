#!/usr/bin/python3
"""
Module that defines a write file fuction
"""


def write_file(filename="", text=""):
    """Writing file"""
    with open(filename, mode="w", encoding="utf-8") as file:
        count = file.write(text)

    return count
