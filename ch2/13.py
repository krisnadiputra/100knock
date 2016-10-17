#! /usr/bin/env python
# -*- coding:utf-8 -*-
# 12.py

import sys

with open("col1.txt") as f1, open("col2.txt") as f2:
    lines1 = f1.readlines();
    lines2 = f2.readlines();

with open("merge.txt","w") as writer:
    for word1,word2 in zip(lines1,lines2):
        writer.write("\t".join([word1.rstrip(),word2]));
