#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 06.py

str1 = "paraparaparadise"
str2 = "paragraph"

def ngram(input, n):
    l = len(input)
    list = []
    input = (n-1)*"$" + input + (n-1)*"$"
    for i in xrange(l+n-1):
        list.append(input[i:i+n])
    return list

X = set(ngram(str1,2))
Y = set(ngram(str2,2))

print X.union(Y)
print X.intersection(Y)
print X.difference(Y)

print "se" in X
print "se" in Y
