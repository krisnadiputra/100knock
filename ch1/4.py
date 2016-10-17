#!/usr/bin/env python
# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.split()

single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

for word in str:
    if str.index(word)+1 in single:
        dict[word[:1]]=str.index(word)+1
    else :
        dict[word[:2]] = str.index(word) + 1

for k,v in sorted(dict.items(), key = lambda x:x[1]):
    print k, v
