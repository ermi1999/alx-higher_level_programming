#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            keys.append(i)
    for i in keys:
        del a_dictionary[i]
    return a_dictionary
