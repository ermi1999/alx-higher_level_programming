#!/bin/bash
# prints You got me!
curl -X PUT -s -o /dev/null -w "You got me!" 0.0.0.0:5000/catch_me
