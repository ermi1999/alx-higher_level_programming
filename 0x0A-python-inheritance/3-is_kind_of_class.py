#!/usr/bin/python3
"""
This Program checks if the object is an instance of or if the object
is an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    This function checks  if the object is an instance of,
    or if    the object is an instance
    of a class that inherited from, the specified class.
    Args:
        obj: The object.
        a_class: The class.
    """
    return isinstance(obj, a_class)
