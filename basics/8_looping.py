#!/usr/bin/python
# coding=utf-8

if __name__ == '__main__':
    names = ['Ana', 'Lili','Costi','Lili','Dany']
    # indice si valoare:
    for i,v in enumerate(names):
        print(i,v)
    # e recomandat sa faci copie cand rulezi prin lista
    for name in names[:]:
        print(name)
    # sau cand vrei sa rulezi in ordine desc sau asc:
    for name in sorted(set(names)):
        print(name)
    # sau daca vrei sa treci prin multiple liste simultan:
    ages=[25,13,12,14,65,44]
    print('############################')
    for name,age in zip(names,ages):
        print(name,age)
    print('############################')
    # dictionare
    dick = dict(Ana=1,Titi=3,George=2)
    for k,v in dick.items():
        print(k,v)
