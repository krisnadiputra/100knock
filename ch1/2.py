#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = u"パトカー"
b = u"タクシー"

for i in range(len(a)+len(b)):
    if i%2:
        print b[i/2]
    else :
        print a[i/2]
