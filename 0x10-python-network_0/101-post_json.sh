#!/bin/bash
# sends a json file as a post request
curl -sX POST -H "Content-Type: application/json" -d @$2 $1
