#!/usr/bin/python
"""this module gets the last 10 commits to a repo"""
import sys
import requests

if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits?limit=10'.format(sys.argv[2], sys.argv[1]))
    i = 0
    objs = res.json()
    for i in range(10):
        print("{}: {}".format(objs[i].get('sha'), objs[i].get('commit').get('author').get('name')))
