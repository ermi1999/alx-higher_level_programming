#!/usr/bin/python3
"""
This program inititalizes a class called MyInt.
"""
class MyInt(int):
    """
    Inverts == and != operators.
    """
    def __eq__(self, num):
        """
        inverts == with !=.
        """
        return self.real != num

    def __ne__(self, num):
        """
        inverts != with ==
        """
        return self.real == num
