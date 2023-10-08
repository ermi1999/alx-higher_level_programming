#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length < 1:
        first_letter = None
    else:
        first_letter = sentence[0]
    result = (length, first_letter)
    return result
