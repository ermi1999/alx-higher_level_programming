#!/bin/bash
# gets the allowed methods
curl -sI $1 | grep -i "Allow" | awk -F': ' '{print $2}'
