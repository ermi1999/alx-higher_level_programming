#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_list = []
    i = 0
    for i, row in enumerate(matrix):
        copy = []
        for j, element in enumerate(row):
            num = element ** 2
            copy.append(num)
        my_list.append(copy)
    return my_list
