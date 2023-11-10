#!/usr/bin/python3
"""
This program intializes a class called Base.
"""
import json


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

    @classmethod
    def to_json_string(cls, list_dictionaries):
        """
        This function returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes JSON string representation of list_objs to a file
        """
        dicts = []
        file_name = "{}.json".format(cls.__name__)
        for obj in list_objs:
            dicts.append(obj.to_dictionary())
        json_str = Base.to_json_string(dicts)
        with open(file_name, "w") as f:
            f.write(json_str)
