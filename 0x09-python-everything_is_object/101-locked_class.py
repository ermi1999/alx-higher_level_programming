#!/usr/bin/python3
"""
This program defines a class tha is called LockedClass.
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """
    this class prevents the user from dynamically
    creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        checks if the attribute assignment is correct.
        and then assigns it.
        """
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '"
                                 + "{}'".format(name))
        super().__setattr__(name, value)
