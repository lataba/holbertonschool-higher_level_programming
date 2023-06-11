#!/usr/bin/python3

def best_score(a_dictionary):
    """function that returns a key with the biggest integer value"""

    biggest = 0
    best_key = None

    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if isinstance(value, int) and value > biggest:
                biggest = value
                best_key = key

    return (best_key)
