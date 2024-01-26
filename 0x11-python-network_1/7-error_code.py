#!/usr/bin/python3
"""sends a request and prints the status code
if the code is greater than or equal to 400
"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code >= 400:
        print(req.status_code)
    else:
        print(req.text)
