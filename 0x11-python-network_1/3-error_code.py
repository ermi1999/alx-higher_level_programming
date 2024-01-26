#!/usr/bin/python3
"""sends a request to the URL and displays the body of the
response (decoded in utf-8)."""
import sys
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        res = urllib.request.urlopen(req)
        print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(e.code)
