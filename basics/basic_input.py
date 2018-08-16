#!/usr/bin/python

print "How old are you?",
age=raw_input()
print "How tall are you?",
height=raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So , you're %r old, %r tall and %r heavy." % (age,height,weight)

first_course=raw_input("First time I used this was with 6.00 at MIT: ")
print "So you studied %s" %first_course

#mom_age=55
#diff = mom_age-age
#print "The diff between mom and me: %d" % diff

print "If you really want a number:"


number=(raw_input("Type it: ")

while isinstance(number, (int, long) ) == False:
    number=raw_input("Type it: ")

print "Looks good %d" % number


