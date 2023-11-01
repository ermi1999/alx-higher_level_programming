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
    result = np.dot(m_a, m_b)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
