#!/usr/bin/python
# coding=utf-8

# Avantajul e ca poti adauga la apel oricat de multe argumente care vor fi 
# puse intr-un tuplu

def f(*meattypes):
    print('Guy likes',meattypes[0])
    print(meattypes)

# Mod clasic de definire a funct
def g(arg1,arg2,arg3):
    print(arg1,' but not ',arg3,' or ',arg2)

if __name__ == '__main__':
    f('asd','chicken','shit')

    #tuple1=('asd','asdsda','ytd','tges')
    tuple1=('asd','asdsda','ytd','23ds') # aici treb sa fii atent la cate chestii pui in tuplu pt ca extinderea nu merge
    f(*tuple1)
    g(*tuple1)
print('''
    Fii atent, cand ai * in argumentul din functie poti pune un numar arbitrar in apelul functiei
''')
