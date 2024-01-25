#!/bin/bash
# sends a json file as a post request
curl -s -X POST -H "Content-Type: application/json" -T "$2" $1
