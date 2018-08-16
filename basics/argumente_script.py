#!/usr/bin/python

# So you import something from a module here 
# I'm saying something but it's a list, with argv[0] being the name of the program
# Alternatively you could do import sys and access the list values by sys.argv[0]

from sys import argv

# fii atent la nr de arg,
# daca ai prea multe primesti:

#ValueError: too many values to unpack

# prea putine:

#ValueError: need more than 1 value to unpack
script,first,second,third = argv

print "Program's name: ",script
print "first arg: ",first
print "second arg: ",second
print "third arg: ",third
