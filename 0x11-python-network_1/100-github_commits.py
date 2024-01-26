#!/usr/bin/python3
"""this module gets the last 10 commits to a repo"""
import sys
import requests

if __name__ == "__main__":
    res = requests.get(
        'https://api.github.com/repos/{}/{}/commits'.format(
            sys.argv[2], sys.argv[1]))
    objs = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                objs[i].get('sha'), objs[i].get(
                    'commit').get('author').get('name')))
    except IndexError:
        pass
