#!/usr/bin/python

tabby = "I'm a \t tabby cat."
persian = 'I\'m a \n newline cat'

# Nu face diferenta daca ai  \\ sau \ la urmatorul rand:
backslash = "I'm a \\ cat."

print(tabby)
print(persian)
print(backslash)


# Nu face diferenta intre 3" si 3' se pare...

print(''' Mary had a little
\t fucking lamb.
It was gay.
She loved it.
''')

# This sends an alert
print("what is this\a,Sergiu?")
# This deletes a char, in this case s from this
print("what is this\b,Sergiu?")
# This puts everyhthing after \f on the next line from the exact position it was before 
print("what is this\f,Sergiu?")
# This deletes everything until \r
print("what is this\r,Sergiu?")
# This kind of looks like \f...?!
print("what is this\v,Sergiu?")

# Vezi ca %r alege un mod eficient de a printa si ar putea sa para ciudat..
a="It's my life\""
print("The %%r format specifier in action: %r " % a)
print("The %%s format specifier in action: %s " % a)

