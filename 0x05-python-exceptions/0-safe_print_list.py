#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for element in my_list:
            if i < x:
                print("{}".format(element), end="")
                i += 1
        print()
        return i
    except IndexError:
        return i
