#!/usr/bin/python
# coding=utf-8

months=12
balance=999999
annualInterestRate=0.2
mir=annualInterestRate/12
#mp = round(round(balance*1.0/months)/10)*10-10
mp=0

current_balance=balance
while current_balance >0 :
    current_balance=balance
    mp +=10
    for month in range(months):
        current_balance = current_balance - mp + mir*(current_balance - mp)
    print mp

print "Lowest Payment:",int(mp)
