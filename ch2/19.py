# ! usr/bin/env python
# -*- coding: utf-8 -*-
# cut -f 1 hightemp.txt | sort | uniq -c | sort -r | cut -c 6-

import sys
from collections import defaultdict

prefectures = defaultdict(int)

with open("hightemp.txt") as f:
    line = f.readline();
    while line:
        prefectures[line.split()[0]]+=1;
        line = f.readline();


for k,v in sorted(prefectures.items(), key= lambda x:x[1], reverse=True):
    print(k);