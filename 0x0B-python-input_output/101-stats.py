#!/usr/bin/python3
"""
This program reads stdin line by line and computes metrics.
"""

import sys

def stats():
    """
    This program reads stdin line by line and computes metrics.
    """
    lines = 10

    try:
        while True:
            status_code = {
                '200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0
            }
            file_size = 0

            for i in range(lines):
                line = sys.stdin.readline().strip()
                words = line.split()
                status_code[words[7]] += 1
                file_size += int(words[8])

            print("File size: {:d}".format(file_size))
            sort = sorted(status_code.keys())
            for key in sort:
                if status_code[key] > 0:
                    print("{:d}: {:d}".format(int(key), status_code[key]))

            lines += 10

    except KeyboardInterrupt:
        print("File size: {:d}".format(file_size))
        sort = sorted(status_code.keys())
        for key in sort:
            if status_code[key] > 0:
                print("{:d}: {:d}".format(int(key), status_code[key]))
        raise

if __name__ == "__main__":
    stats()
