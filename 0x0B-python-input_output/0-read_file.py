#!/usr/bin/python3
"""
This Program reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    This function reads file and prints it to stdout.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
