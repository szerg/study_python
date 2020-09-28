#!/usr/bin/python

from sys import argv
from os.path import isfile

if isfile(argv[1]):
    open(argv[2],'w').write(open(argv[1]).read())
else:
    print("Source file does not exist!")
