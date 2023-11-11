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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list of the
        JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes JSON string representation of list_objs to a file
        """
        dicts = []
        file_name = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
        json_str = cls.to_json_string(dicts)
        with open(file_name, "w") as f:
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        This function returns an instance with all attributes already set.
        """
        new = cls(4, 4)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        This function returns a list of instances
        """
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, "r") as f:
                json_read = f.read()
        except FileNotFoundError:
            return []
        dict_repr = cls.from_json_string(json_read)
        array_of_instances = []
        for item in dict_repr:
            array_of_instances.append(cls.create(**item))
        return array_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This funnction handles the writes list of objects to csv file.
        """
        dicts = []
        file_name = "{}.csv".format(cls.__name__)
        if list_objs is not None:
            for obj in list_objs:
                dicts.append(obj.to_dictionary())
        json_str = cls.to_json_string(dicts)
        with open(file_name, "w") as f:
            f.write(json_str)

    @classmethod
    def load_from_file_csv(cls):
        """
        This function loads a file and returns a list of instances.
        """
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, "r") as f:
                json_read = f.read()
        except FileNotFoundError:
            return []
        dict_repr = cls.from_json_string(json_read)
        array_of_instances = []
        for item in dict_repr:
            array_of_instances.append(cls.create(**item))
        return array_of_instances
