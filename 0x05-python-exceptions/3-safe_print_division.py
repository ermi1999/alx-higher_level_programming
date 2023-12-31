#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: {}".format(result))
        return result
    finally:
        if result is not None:
            print("Inside result: {}".format(round(result, 2)))
        return result
