#!/usr/bin/python
# coding=utf-8

months=12
orig_balance=999999
balance=orig_balance
air=0.18

mir=air/12
low=balance/12
high=balance*(1+mir)**12/12

mp=(low+high)/2
while abs(balance)>0.01:
    balance=orig_balance
    for i in range(months):
        balance=balance-mp+(balance - mp)*mir
    if balance > 0:
        low = mp
    if balance < 0:
        high = mp
    mp=(low+high)/2
print  "Lowest Payment:",round(mp,2)
