#!/usr/bin/python3
"""posts an email and prints the response the email and the
url are passed as an argument
"""
import sys
import responses

if __name__ == "__main__":
    res = responses.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
