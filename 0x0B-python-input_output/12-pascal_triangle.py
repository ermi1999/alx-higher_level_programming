#!/usr/bin/python3
"""
This program returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Args:
        n: the triangle size.
    """
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            element = pascal[i - 1][j - 1] + pascal[i - 1][j]
            row.append(element)
        row.append(1)
        pascal.append(row)
    return pascal
