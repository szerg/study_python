#!/usr/bin/python
# coding=utf-8
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr)==0:
        return False
    if len(aStr)==1:
        return char == aStr
    if char < aStr[len(aStr)/2]:
        return isIn(char,aStr[:len(aStr)/2])
    elif char > aStr[len(aStr)/2]:
        return isIn(char,aStr[len(aStr)/2:])
    else:
        return True

if __name__ == '__main__':
        print isIn('v','cdejjllttuwxyy')

