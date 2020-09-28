#!/usr/bin/python

from sys import argv

script,filename = argv

# This actually truncates the whole file so no need to call truncate afterwards
fw = open(filename,'r+')

print(fw.read())

# Now add something at the end because that's where you are with the seek. This does not create a new line

fw.write("Shit load !!")
fw.write("Shit load again!!")


fw.close()
