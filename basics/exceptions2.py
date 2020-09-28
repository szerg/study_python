#!/usr/bin/python
# coding=utf-8

def sum_string(s):
    '''Ar tb sa returneze suma numerelor aflate in s, de ex pt a2b34c returneaza 9; dar daca ai vrea sa returneze 36 ? :)'''
    assert s!=None, "s is None"
    res=0
    for char in s:
        try:
            nr = int(char)
            res+=nr
        except(ValueError):
            continue
            
    return res

if __name__ == '__main__':
#    test_suite = ['1234','a13x0',None,'']
    test_suite = ['1234','a13x0','']
    for s in test_suite:
        print(sum_string(s))
    









