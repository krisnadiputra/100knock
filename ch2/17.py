# !usr/bin/env python
# -*- coding: utf-8 -*-
# cut -f 1 hightemp.txt | sort | uniq

import sys

prefectures = set();

with open("hightemp.txt") as f:
    line = f.readline();
    while line:
        prefectures.add(line.split()[0])
        line = f.readline()

for pref in prefectures:
    print (pref)

