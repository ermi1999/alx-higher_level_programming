#!/usr/bin/python3
"""get a value from the header"""
import sys
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
