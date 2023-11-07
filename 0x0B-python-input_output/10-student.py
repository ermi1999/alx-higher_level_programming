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
        json = {}
        i = 0
        for name, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                if (isinstance(attrs, list) and
                        all(isinstance(item, str) for item in attrs)):
                    for i in attrs:
                        if i == name:
                            json[name] = value
                    continue
                json[name] = value
        return json
