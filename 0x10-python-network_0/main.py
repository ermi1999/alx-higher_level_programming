#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

a = [5, 4, 3, 2, 1]
answers = [5]

for i in range(100):
    res = find_peak(a)
    if res not in answers:
        print("Wrong answer")
        exit(1)

print("OK", end="")
