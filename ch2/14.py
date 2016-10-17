# !/usr/bin/env python
# -*- coding: utf-8 -*-
# head -2 hightemp.txt


import sys

with open(sys.argv[1]) as f:
    lines = f.readlines();

n = sys.argv[2];

print "".join(lines[0:int(n)])
