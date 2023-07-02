#!/usr/bin/python3
"""
Class definition
"""
import json


class Base:
    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries == "None" or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)
