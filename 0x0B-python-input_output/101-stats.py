#!/usr/bin/python3
"""
This program reads stdin line by line and computes metrics.
"""

def stats():
    """
    This program reads stdin line by line and computes metrics.
    """
    status_code = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
    }
    file_size = 0
    lines = 10
    try:
        while (True):
            i = 0
            while (i < lines):
                line = input()
                words = line.split()
                status_code[words[7]] += 1
                file_size += int(words[8])
                i += 1
            print("File size: {:d}".format(file_size))
            sort = sorted(status_code.keys())
            for key in sort:
                if status_code[key] > 0:
                    print("{:d}: {:d}".format(int(key), status_code[key]))
    except KeyboardInterrupt:
        print("File size: {:d}".format(file_size))
        sort = sorted(status_code.keys())
        for key in sort:
            if status_code[key] > 0:
                print("{:d}: {:d}".format(int(key), status_code[key]))
        raise
if __name__ == "__main__":
    stats()