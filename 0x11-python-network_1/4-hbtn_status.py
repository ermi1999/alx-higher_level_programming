#!/usr/bin/python3
"""sends a get request using requests package"""
import requests

if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as req:
        print("Body response:\n\t- type: {}\n\t- content: {}".format(
              type(req.text), req.text))
