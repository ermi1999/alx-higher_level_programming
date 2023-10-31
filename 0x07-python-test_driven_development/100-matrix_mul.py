#!/usr/bin/python3
"""
This program multiplies 2 matrices.
and returns the result.
"""


def matrix_mul(m_a, m_b):
    """
    this function multiplies 2 matrices.
    Args:
        m_a: list of lists of integers or floats.
        m_b: list of lists of integers or floats
    Returns:
        A list of lists after multiplication.
    Raises:
        TypeError: if one of the list of lists is not an int or float.
        or one of the arguments is not a list of lists.
        ValueError: if m_a or m_b cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    for row in m_a:
        if not row:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if not row:
            raise ValueError("m_b can't be empty")
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

    rows_m_a = len(m_a)
    cols_m_a = len(m_a[0])
    rows_m_b = len(m_b)
    cols_m_b = len(m_b[0])
    if cols_m_a != rows_m_b:
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for i in range(cols_m_b)] for j in range(rows_m_a)]
    for i in range(rows_m_a):
        for j in range(cols_m_b):
            for k in range(cols_m_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
