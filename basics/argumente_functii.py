#!/usr/bin/python
# coding=utf-8

# default args
def info(name='Gogu',age=5):
    print "His name is",name,"and he is",age

def info_again(name,age,weight):
    print "His name is %s and he is %d and he weighs %d" %(name,age,weight)

if __name__ == '__main__':
    # poate fi apelat fara parametri
    info()
    # sau cu unul din ele
    info('Cristi')

    params = ['Ion',14,70]
    # asta e tare pt ca poti transforma lista in argumentele pozitionale(face expand)
    info_again(*params)


