#!/usr/bin/python3
"""this module finds the X-Request-Id header
    value in a url that is given as an argument.
"""
import sys
import requests

if __name__ == "__main__":
    with requests.get(sys.argv[1]) as req:
        print(req.headers['X-Request-Id'])
