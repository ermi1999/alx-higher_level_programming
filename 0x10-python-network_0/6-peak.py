#!/usr/bin/python3
"""Module to find the peak of a list of integers"""


def find_peak(list_of_integers):
    """Finds the peak number in a list"""
    if len(list_of_integers) == 0:
        return None
    peaks = []
    i = 0
    while i < len(list_of_integers):
        if i == 0:
            if list_of_integers[i] >= list_of_integers[i + 1]:
                peaks.append(list_of_integers[i])
            i += 1
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] >= list_of_integers[i - 1]:
                peaks.append(list_of_integers[i])
            i += 1
        elif list_of_integers[i] >= list_of_integers[i - 1] and \
                list_of_integers[i] >= list_of_integers[i + 1]:
            peaks.append(list_of_integers[i])
            i += 1
        else:
            i += 1
    if len(peaks) > 0:
        return max(peaks)
    else:
        return None
