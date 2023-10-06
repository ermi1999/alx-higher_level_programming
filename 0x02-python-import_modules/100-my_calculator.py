#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arguments = sys.argv[1:]
    if len(arguments) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(arguments[0])
        b = int(arguments[2])
        operator = arguments[1]

        if operator == "+":
            addition = add(a, b)
            print("{} + {} = {}".format(a, b, addition))
        elif operator == "-":
            subtraction = sub(a, b)
            print("{} - {} = {}".format(a, b, subtraction))
        elif operator == "*":
            multiplication = mul(a, b)
            print("{} * {} = {}".format(a, b, multiplication))
        elif operator == "/":
            division = div(a, b)
            print("{} / {} = {}".format(a, b, division))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
