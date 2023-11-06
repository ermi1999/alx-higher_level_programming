#!/usr/bin/python3
"""
This program will add a new attribute to class.
"""


def add_attribute(cl, var, name):
    """
    This function will add a new attribute to class.
    """
    if not hasattr(cl, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(cl, var, name)
