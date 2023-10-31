#!/usr/bin/python3
"""
This program multiplies 2 matrices by using the module NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices by using the module NumPy.
    Args:
        m_a: The first matrix.
        m_b: The second matrix
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    for row in m_a:
        if not row:
            raise ValueError("m_a can't contain empty lists")
    for row in m_b:
        if not row:
            raise ValueError("m_b can't contain empty lists")
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for first in m_a:
        for others in m_a:
            if len(first) != len(others):
                raise TypeError("each row of m_a must be of the same size")
        break
    for first in m_b:
        for others in m_b:
            if len(first) != len(others):
                raise TypeError("each row of m_b must be of the same size")
        break

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = np.dot(m_a, m_b)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("project/tests/101-lazy_matrix_mul.txt")
