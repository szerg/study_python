#!/usr/bin/python
# coding=utf-8


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    result = 0
    while b ** result <=x:
        result +=1
    return result-1


def f(s):
    return 'a' in s

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for i,s in enumerate(L[:]):
        if not f(s):
            L.remove(s)
    return len(L)

if __name__ == '__main__':
        #print myLog(1,2)
        #print myLog(27,3)
        #print myLog(15,3)
        #L = ['a', 'b', 'a']
        #L = ['ant', 'bing', 'salt']
        #L=['']
        #L=['a']
        L=['b']
        L=['abc', 'bcd', 'def', 'gha']
        print satisfiesF(L)
        print L
