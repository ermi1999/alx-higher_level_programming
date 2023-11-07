#!/usr/bin/python3
"""
This program returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object (string)
    Args:
        my_obj: the object.
    """
    return json.dumps(my_obj)
