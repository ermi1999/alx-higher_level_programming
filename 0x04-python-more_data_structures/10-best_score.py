#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    key = ""
    if not a_dictionary:
        return None
    for i in a_dictionary:
        if a_dictionary[i] > best:
            best = a_dictionary[i]
            key = i
    return key
