#!/usr/bin/python
# coding=utf-8

nr_months=12
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# balance - e deja definit, soldul
# annualInterestRate - dobanda anuala
# monthlyPaymentRate - rata lunara
monthlyInterestRate = annualInterestRate/12
#updatedBalance = balance
totalPaid = 0
for month in range(1,nr_months+1):
    monthlyPay = balance*monthlyPaymentRate
    totalPaid+=monthlyPay
    balance = balance - monthlyPay + monthlyInterestRate * (balance - monthlyPay)
    print "Month:",month
    print "Minimum monthly payment:",round(monthlyPay,2)
    print "Remaining balance: ",round(balance,2)
print "Total paid:",round(totalPaid,2)
print "Remaining balance:",round(balance,2)




