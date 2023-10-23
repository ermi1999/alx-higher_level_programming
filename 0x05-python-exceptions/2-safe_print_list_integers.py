#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        i = 0
        while (i < x):
            if isinstance(my_list[i], int):
                try:
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
                    i += 1
                except IndexError:
                    raise IndexError("IndexError: list index out of range")
            else:
                i += 1
                continue
        print()
        return count
    except IndexError:
        raise
