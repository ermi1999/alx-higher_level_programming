#!/usr/bin/python3
"""this module takes github credentials
as an argument (username) and (password) and prints their id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get('https://api.github.com/user', auth=auth)
    print(res.json().get('id'))
