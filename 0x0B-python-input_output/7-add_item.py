#!/usr/bin/python3
"""
This program adds all arguments to a Python list,
and then save them to a file.
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
my_list = []

try:
    with open(filename, encoding="utf-8") as f:
        my_list = json.loads(f.read())
except Exception:
    my_list = []

i = 1
while (i < len(sys.argv)):
    my_list.append(sys.argv[i])
    i += 1

save_to_json_file(my_list, filename)
load_from_json_file(filename)
