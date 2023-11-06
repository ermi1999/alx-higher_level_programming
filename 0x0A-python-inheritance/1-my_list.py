#!/usr/bin/python3
"""
this program prints a list in sorted order.
"""


class MyList(list):
    """
    this class prints a list in sorted order.
    Args:
        list: the list.
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
