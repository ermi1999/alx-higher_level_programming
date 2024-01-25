#!/bin/bash
# This script takes a url as an argument and sends an http request and returns the size of the body.
curl -sI $1 | grep -i "Content-Length" | awk '{print $2}'
