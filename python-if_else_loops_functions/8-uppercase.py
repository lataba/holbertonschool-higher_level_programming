#!/usr/bin/python3

def uppercase(str):

    string = ""

    for letter in str:
        if (ord(letter) >= 97) and (ord(letter) <= 122):
            string = string + chr(ord(letter) - 32)
        else:
            string = string + letter
    print("{}".format(string))
