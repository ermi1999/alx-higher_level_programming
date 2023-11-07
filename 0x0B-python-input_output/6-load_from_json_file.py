#!/usr/bin/python3
"""
This program creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from a “JSON file”.
    Args:
        filename: The filename.
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
