#!/usr/bin/python3
"""
Module containing the function lookup
"""


def lookup(obj):
    """
    lookup function returns the list of available attributes and methods of an object
    """
    return dir(obj)
