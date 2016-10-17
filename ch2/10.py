#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 10.py

#wc -l filename : hasilnya beda 1 ???

import sys

f= open("hightemp.txt");
line = f.readlines();
f.close()

print len(line)

