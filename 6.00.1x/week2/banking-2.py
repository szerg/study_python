#!/usr/bin/python
# coding=utf-8

months=12
balance=3926
annualInterestRate=0.2
mir=annualInterestRate/12
low = round(round(balance*1.0/months)/10)*10
high =2*low

mp=(low+high)/2
prev_balance=0
current_balance= balance
while prev_balance != current_balance:
    prev_balance = current_balance
    current_balance= balance
    for month in range(months):
        current_balance = current_balance - mp + mir*(current_balance - mp)
    if current_balance > 0:
        low=mp
    if current_balance < 0 and prev_balance != current_balance:
        high=mp
    mp=round(round((low+high)/2)/10)*10

print "Lowest Payment:",int(mp)
