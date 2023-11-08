#!/usr/bin/python3
"""
This program reads stdin line by line and computes metrics.
"""
import sys


def print_stats(status_code, size):
    """
    This function handle the printing of the stats.
    """
    print("File size: {}".format(size))
    sort = sorted(status_code.keys())
    for key in sort:
        if status_code[key] > 0:
            print("{}: {}".format(key, status_code[key]))


def stats():
    """
    This function reads stdin line by line and computes metrics.
    """
    lines = 0
    size = 0
    status_code = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }
    try:
        for line in sys.stdin:
            if lines == 10:
                print_stats(status_code, size)
                lines = 1
            else:
                lines += 1
            line = line.split()
            try:
                size += int(line[8])
            except (IndexError, ValueError):
                raise
            try:
                if line[7] in list(status_code.keys()):
                    status_code[line[7]] += 1
            except IndexError:
                pass

        print_stats(status_code, size)

    except KeyboardInterrupt:
        print_stats(status_code, size)
        raise


if __name__ == "__main__":
    stats()
