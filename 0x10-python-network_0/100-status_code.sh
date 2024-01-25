#!/bin/bash
# prints only the response code
curl -o /dev/null -sw '%{response_code}' $1
