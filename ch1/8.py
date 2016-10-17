#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 08.py

str = "Hello this is our group who are studying NLP100knock."

def chiper(input):
    output=""
    for i in str:
        output += chr(219- ord(i)) if i.islower() else i
    return output

str=chiper(str)
print str

str=chiper(str)
print str