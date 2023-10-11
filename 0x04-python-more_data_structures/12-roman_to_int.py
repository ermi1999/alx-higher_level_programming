#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if not roman_string or roman_string == str:
        return None
    else:
        for i in roman_string:
            if i == "M":
                result += 1000
            elif i == "D":
                result += 500
            elif i == "C":
                result += 100
            elif i == "L":
                result += 50
            elif i == "X":
                result += 10
            elif i == "V":
                result += 5
            elif i == "I":
                result += 1
    return result

