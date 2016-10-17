# #!/usr/bin/env python
# -*- coding: utf-8 -*-
# 11.py

# cat hightemp.txt | tr "\t" " "

import sys

f = open("hightemp.txt")
str = f.read()
f.close()

print str.replace("\t"," ");
