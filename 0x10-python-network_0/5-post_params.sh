#!/bin/bash
# send a post request with parameters.
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
