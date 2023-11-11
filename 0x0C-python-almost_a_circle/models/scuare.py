#!/usr/bin/python3
"""
This program defines a class called Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class initializes a object named Square that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        This function initializes the instances of Square.
        Args:
            size: the size of the square.
            x: the x axis.
            y: the y axis.
            id: The id of the object.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns the string representation of the object.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        the size getter.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        the size setter.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of this class.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of the class
        """
        dict_repr = {
                'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y
        }
        return dict_repr
