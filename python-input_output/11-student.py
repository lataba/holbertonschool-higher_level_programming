#!/usr/bin/python3
"""
 Defines a class 'Student'
"""


class Student:
    """The class Student definition"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            new = {}
            for x in attrs:
                if hasattr(self, x):
                    new[x] = getattr(self, x)
            return new
        return self.__dict__

    def reload_from_json(self, json):
        for x in json.keys():
            setattr(self, x, json[x])
