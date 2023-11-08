#!/usr/bin/python3
"""
This program reads stdin line by line and computes metrics.
"""


status_code = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
file_size = 0
lines = 10
while (True):
    i = 0
    while (i < lines):
        line = input()
        words = line.split()
        status_code[words[7]] += 1
        file_size += int(words[8])
        i += 1
    print("File size: {}".format(file_size))
    sort = sorted(status_code.keys())
    for key in sort:
        if status_code[key] > 0:
            print("{}: {}".format(key, status_code[key]))
