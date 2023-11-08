#!/usr/bin/python3
"""
This program inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function appends after a specific string.
    Args:
        filename: the name of the file.
        search_string: the string to search.
        new_string: The new string.
    """
    with open(filename, mode="r+", encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)

        for line in lines:
            f.write(line)

            if search_string in line:
                f.write(new_string)

        f.truncate()
