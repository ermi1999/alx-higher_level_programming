#!/usr/bin/python3
def islower(c):
    lower = 0
    for i in range(97, 123):
        if chr(i) == c:
            lower = 1
    if lower == 1:
        return True
    else:
        return False
