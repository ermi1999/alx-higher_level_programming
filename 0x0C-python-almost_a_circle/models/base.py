#!/usr/bin/python3
"""
This program intializes a class called Base.
"""


class Base:
    """
    This program intializes a class called Base.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.
        Args:
            id: id of classes.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
