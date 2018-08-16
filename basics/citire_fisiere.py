#!/usr/bin/python

from sys import argv

script,filename = argv

# This goes by default to reading
txt = open(filename,'r+')

print "Here's the file: %r" % filename
print txt.read() # This reads the whole file so be careful if it's a big one

# return to the beginning
txt.seek(0,0)

# This reads the file with each line in a string. It could be useful
print txt.readlines()

# return to the beginning
txt.seek(0,0)

# this reads a line
print txt.readline()
# current file pos
print txt.tell()
# this truncates the file from the current position showed by tell onward; cool :)
txt.truncate()

txt.close()

#
#print "Type the filename again"
#file_again = raw_input(">")
#
#txt_again=open(file_again)
#print txt_again.read()
#
#txt_again.close()


