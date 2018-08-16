#!/usr/bin/python
# coding=utf-8

def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        print x,a
        return x
    else:
        rem(x-a, a)

if __name__ == '__main__':
        print rem(7,5)

