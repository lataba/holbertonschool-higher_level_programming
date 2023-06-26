#!/usr/bin/python3
"""
Defines a function that returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Function JSON to Python"""

    return json.loads(my_str)
