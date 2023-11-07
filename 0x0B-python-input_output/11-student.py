#!/usr/bin/python3
"""
This program initializes a class called Student.
"""


class Student:
    """
    Inititalizes a class called student.
    """
    def __init__(self, first_name, last_name, age):
        """
        This function intializes a first name, last name and age for person.
        Args:
            first_name: The first name.
            last_name: The last name
            age: The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    json_dict[attr] = self.__dict__[attr]
            return json_dict

    def reload_from_json(self, json):
        """
        This function replaces all attributes of the Student instance.
        Args:
            json: the json file.
        """
        for key, value in json.items():
            setattr(self, key, value)
