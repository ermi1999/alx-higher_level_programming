#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    used = []
    for i in my_list:
        if i not in used:
            result += i
            used.append(i)
    return result
