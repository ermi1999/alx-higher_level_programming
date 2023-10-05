#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    addition = add(a, b)
    print("{} + {} = {}".format(a, b, addition))
    subtraction = sub(a, b)
    print("{} - {} = {}".format(a, b, subtraction))
    multiplication = mul(a, b)
    print("{} * {} = {}".format(a, b, multiplication))
    division = div(a, b)
    print("{} / {} = {}".format(a, b, division))
