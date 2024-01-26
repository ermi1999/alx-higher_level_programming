#!/usr/bin/python3
"""this module fetches a url and prints the information."""
from urllib import request
if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(content), content, content.decode('utf-8')))
