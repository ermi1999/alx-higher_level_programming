#!/usr/bin/python3
"""this module takes a letter as argument and sends a post request."""
import sys
import requests

if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        js = req.json()
        if len(js) > 0:
            print("[{}] {}".format(js.get('id'), js.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
