#!/usr/bin/python3
"""Module to find the peak of a list of integers"""


def find_peak(list_of_integers):
    """Finds the peak number in a list"""
    if len(list_of_integers) == 0:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
