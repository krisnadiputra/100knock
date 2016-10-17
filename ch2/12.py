#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 12.py

#cut -f 1 filename

import sys

def colwrite(lines, colnum, outfile):
    newcol =[]
    for line in lines:
        newcol.append(line.split()[colnum]+"\n");
    with open(outfile, "w") as writer:
        writer.writelines(newcol);

f = open("hightemp.txt");
lines = f.readlines()
f.close()

colwrite(lines, 0, "col1.txt")
colwrite(lines, 1, "col2.txt")