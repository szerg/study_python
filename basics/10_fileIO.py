#!/usr/bin/python
# coding=utf-8

import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename,'w') as filehandle:
        filehandle.write("Fllowing best practices!")
    print(filehandle.closed) # check if indeed closed

