# !usr/bin/env python
# -*- coding: utf-8 -*-
# sort -r -k 3 hightemp.txt

import sys

with open("hightemp.txt") as f:
    lines = f.readlines();

for line in sorted(lines, key=lambda x:x.split()[2], reverse=True):
    print line.rstrip("\n");
