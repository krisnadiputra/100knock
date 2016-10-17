# !/usr/bin/env python
# -*- coding:utf-8 -*-
# split -l 8 hightemp.txt

import sys

def splitfiles(filename, nfile):
    with open(filename) as f:
        lines = f.readlines();

    if len(lines)%nfile !=0 :
        raise Exception("cannot divide the file!")
    else:
        nline = len(lines)/nfile;
        for i in xrange(nfile):
            with open("split%s.txt" % str(i), "w") as writer:
                writer.writelines(lines[i*nline:nline*(i+1)]);

if __name__=="__main__":
    try:
        splitfiles(sys.argv[1], int(sys.argv[2]));
    except Exception as err:
        print ("Err: ", err)