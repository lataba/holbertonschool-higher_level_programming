#!/usr/bin/python3
"""
Defines a function that writes an Object to a text file, using a JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """Object to text file using JSON"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
