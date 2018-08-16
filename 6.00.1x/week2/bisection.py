#!/usr/bin/python
# coding=utf-8

print 'Please think of a number between 0 and 100!'
low = 0
high = 100
ans = (low+high)/2
x= raw_input("Is your secret number "+str(ans)+"?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly. ")
answers=['h','l','c']
while x!='c':
    while x not in answers:
        print "Sorry, I did not understand your input."
        x= raw_input("Is your secret number "+str(ans)+"?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly. ")
    if x == 'l':
        low = ans
    elif x == 'h':
        high = ans
    else:
        break
    ans = (high + low)/2
    x= raw_input("Is your secret number "+str(ans)+"?\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly.")
print "Game over. Your secret number was:",str(ans)

