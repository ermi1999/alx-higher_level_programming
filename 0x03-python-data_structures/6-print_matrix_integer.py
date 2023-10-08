#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 0
        for j in i:
            if k == len(i) - 1:
                print("{:d}".format(j), end="")
                k += 1
            else:
                print("{:d}".format(j), end=" ")
                k += 1
        print()
