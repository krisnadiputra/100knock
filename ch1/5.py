#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 05.py

#zip(*[sentence[i:] for i in range(n)])

original = "I am an NLPer"

def ngram(input, n):
    l = len(input)
    if type(input) == str:
        input = (n-1)*"$" + input + (n-1)*"$"
        for i in xrange(l+n-1):
            print input[i:i+n];
    elif type(input) == list:
        input = (n - 1) *["$"] + input + (n - 1) * ["$"]
        for i in xrange(l + n - 1):
            print input[i:i + n];

ngram(original, 2)
original = original.split()
ngram(original, 2)
