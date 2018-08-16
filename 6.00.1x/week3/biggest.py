#!/usr/bin/python
# coding=utf-8

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxim=0
    kmaxim=None
    for k in aDict.keys():
        if len(aDict[k]) >= maxim:
            maxim=len(aDict[k])
            kmaxim=k
    return kmaxim

if __name__ == '__main__':
    print biggest({'a': [17, 2], 'c': [1], 'b': [18, 12, 3, 6, 14, 7, 7, 19, 1, 5], 'e': [4, 6, 17, 5, 0, 5, 6], 'd': [4, 17, 13, 9, 2, 7, 12, 15]})
    print biggest({'a':[]})    
    print biggest({})    
