#!/usr/bin/python3
"""
This program initializes a class named Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class initializes a object named Rectangle that inherits from base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This function initializes the class instances.
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            x: the x axis.
            y: The y axis.
            id: the class id.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 1:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """
        returs the width
        """
        return self.__width

    @property
    def height(self):
        """
        Returns the height.
        """
        return self.__height

    @property
    def x(self):
        """
        Returns the x value
        """
        return self.__x

    @property
    def y(self):
        """
        Returns the y value
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets the width instance.
        Args:
            value: The value of width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height instance.
        Args:
            value: The value of height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the x instance.
        Args:
            value: The value of x.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the y instance.
        Args:
            value: The value of y.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        prints the rectangle instance to stdout using #.
        """
        for new_line in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Updates the class Rectangle attributes.
        Args:
            args: The arguments.
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dectionary representation of the class.
        """

        dict_repr = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return dict_repr
