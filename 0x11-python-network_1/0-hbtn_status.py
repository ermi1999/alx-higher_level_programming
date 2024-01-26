#!/usr/bin/python3
"""this module fetches a url and prints the information."""
from urllib import request

with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(content), content, content.decode('utf-8')))
