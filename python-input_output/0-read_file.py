#!/usr/bin/python3
"""
Module that defines a read file fuction
"""


def read_file(filename=""):
    """Reading file"""
    with open(filename, mode="r", encoding="UTF8") as file:
        print(file.read(), end="")
