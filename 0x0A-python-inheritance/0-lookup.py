#!/usr/bin/python3
"""
this program returns a list of available attributes and methods
of an object.
"""


def lookup(obj):
    """
    returns a list of available attributes and methods of an object.
    Args:
        obj: The object.
    """
    return dir(obj)
