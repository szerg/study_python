#!/usr/bin/python
# coding=utf-8

if __name__ == '__main__':
        s='abcbcd'
        longest=''
        list_of_longest=[]
        for i,v in enumerate(s):
                longest=v
                j=i+1
                while(j<len(s)):
                        if s[j] >= v:
                                longest=longest+s[j]
                                v=s[j]
                                j+=1
                        else:
                                break
                list_of_longest.append((longest,len(longest)))
        maxim=('',0)
        for pair in list_of_longest:
            if maxim[1] < pair[1]:
                maxim=pair
        print "Longest substring in alphabetical order is:",maxim[0]

