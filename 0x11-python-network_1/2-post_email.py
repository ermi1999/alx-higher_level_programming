#!/usr/bin/python3
"""accepts url and email as an argument and sends a post request"""
import sys
import urllib.request

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))

