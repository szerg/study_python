#!/usr/bin/python
# coding=utf-8

# cu asta faci cozi ca listele sunt ineficiente daca faci cozi din ele
# sunt in schimb f ok daca vrei sa faci stack-uri
from collections import deque

def f(x):
    return x**2 <= 100
def g(x,y):
    return x+y

if __name__ == '__main__':
    list1=[1,2,3]
    list2=[1,2,3]
    list1.append(list2)
    print list1
    list1.pop()
    print list1
    list1.append(list2[1])
    print list1.index(2)
    print list1.count(2)
    list1.sort()
    print list1
    list1.reverse()
    print list1

    myqueue = deque([1,2,3])
    print myqueue
    print myqueue.popleft()
    for elem in myqueue:
        print elem

# functiile alea: map,reduce,filter sunt f tari
    # filter returneaza toate elem pt care functia f e adevarata
    print filter(f,[4,7,10,234,12])
    # map returneaza rezultatul functiei f apelata pe toate elem
    print map(f,[11,2,33,10])
    # reduce aplica functia f pe primele 2 elem din lista data ca argument , apoi aplica iar f pe rezultat si urmatorul element si tot asa
    print reduce(g,[2,4,5])

# list comprehensions: moduri rapide de a crea liste, fara sa scrii mult
    squares = [x**2 for x in range(10)]
    print squares
    different = [x for x in [1,3,5] if x not in [2,3,7,8]]
    print different
# set - alta structura smechera pentru ca contine doar elemente unice si permite operatii de tip a|b (element in setul a sau b) a-b (element in setul a dar nu si in b)
    numbers = (1,2,2,43,213,51,43)
    numbers_unique = set(numbers)
    print numbers_unique
