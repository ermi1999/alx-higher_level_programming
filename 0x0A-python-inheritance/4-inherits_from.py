#!/usr/bin/python3
"""
This program checks if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    This function checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class.
    Args:
        obj: The object.
        a_class: The class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
