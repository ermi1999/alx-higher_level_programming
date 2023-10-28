#!/usr/bin/python3
"""
this program divides all elements of a matrix list.
if the list passed to it must be a list of lists of integers or floats,
otherwise TypeError is raised.
the second argument has to be a number greater than 0.
if the above requirements fulfiled a new list is returned with the results.
"""


def matrix_divided(matrix, div):
    """
    this function divides all elements of a matrix list.
    Args:
        matrix: (list) the list
        div: (int) the dividor
    Returns:
        List: a list with numbers after the division
    Raises:
        TypeError: if matrix is a list of lists
        TypeError: if matrix elements are not integers or floats
        ZeroDivisionError: if the div is 0
        TypeError: if div is not a number
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    row1 = matrix[0]
    for row in matrix:
        if len(row) != len(row1):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [row[:] for row in matrix]
    row = 0
    for i, row, in enumerate(matrix):
        for j, element in enumerate(row):
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
