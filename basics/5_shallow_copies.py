#!/usr/bin/python
# coding=utf-8

if __name__ == '__main__':
    # evident asta schimba ambele liste
    firstlist = ['ana', 'titi', 'costel']
    secondlist = firstlist
    secondlist[0] = 'andrei'
    print(firstlist)

    # asta face o noua copie
    secondlist = firstlist[:]
    secondlist[0] = 'afnic.nat'
    print(firstlist)
    print(secondlist)
