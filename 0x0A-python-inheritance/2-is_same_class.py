#!/usr/bin/python3
"""
This program checks if an object is exactly an
instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is
    exactly an instance of the specified class otherwize false.
    Args:
        obj: The object.
        a_class: The class.
    """
    return type(obj) is a_class
