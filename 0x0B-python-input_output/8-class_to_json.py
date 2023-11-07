#!/usr/bin/python3
"""
This program returns the dictionary description with simple data structure.
"""


def class_to_json(obj):
    """
    This function returns the dictionary description.
    """
    json = {}
    for name, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json[name] = value
    return json
