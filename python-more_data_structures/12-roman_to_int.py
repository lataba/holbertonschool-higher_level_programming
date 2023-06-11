#!/usr/bin/python3

def roman_to_int(roman_string):
    """function that converts a Roman numeral to an integer"""

    if not roman_string or (not isinstance(roman_string, str)):
        return (0)

    r_values = {"I": 1, "V": 5, "X": 10, "L": 50,
                "C": 100, "D": 500, "M": 1000}

    result = 0

    for i in range(len(roman_string)):
        if r_values.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                r_values[roman_string[i]] < r_values[roman_string[i + 1]]):
            result = result + r_values[roman_string[i]] * -1

        else:
            result = result + r_values[roman_string[i]]

    return (result)
