#!/usr/bin/python3
"""
Defines a function that returns the dictionary description”
"""


def class_to_json(obj):
    """Return the dictionary"""
    return obj.__dict__
