#!/usr/bin/python3
"""
Defines a function that creates an Object from a “JSON file”
"""
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    it = load_from_json_file("add_item.json")
except FileNotFoundError:
    it = []
for i in range(1, len(sys.argv)):
    it.append(sys.argv[i])
save_to_json_file(it, "add_item.json")
