#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) < 1:
            return None
        else:
            result = 0
            for i in my_list:
                if i > result:
                    result = i
            return result
