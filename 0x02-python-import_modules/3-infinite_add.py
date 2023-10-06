#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0
    arguments = sys.argv[1:]
    converted = [eval(i) for i in arguments]
    for i in range(0, len(converted)):
        result = converted[i] + result
    print (result)
