#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    copy = my_list
    result = list(map(lambda x: x * number, copy))
    return result
