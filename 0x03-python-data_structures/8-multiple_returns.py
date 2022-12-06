#!/usr/bin/python3


def multiple_returns(sentence):
    if len(sentence) == 0:
        fst = None
    else:
        fst = sentence[0]
    return (len(sentence), fst)
