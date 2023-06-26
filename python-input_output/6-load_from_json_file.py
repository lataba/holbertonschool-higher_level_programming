#!/usr/bin/python3
"""
Defines a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Creating the Object from JSON file"""
    with open(filename, "r") as file:
        return json.load(file)
