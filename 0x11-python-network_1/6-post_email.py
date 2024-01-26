#!/usr/bin/python3
"""posts an email and prints the response the email and the
url are passed as an argument
"""
import sys
import requests

if __name__ == "__main__":
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
