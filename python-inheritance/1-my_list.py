#!/usr/bin/python3
"""
Defines a class that inherits from list
"""


class MyList(list):
    """
    Creating a list
    """

    def print_sorted(self):
        """
        Print a list
        """
        sort_list = sorted(self)
        print(sort_list)
