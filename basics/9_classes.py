#!/usr/bin/python
# coding=utf-8

class Bloc:
    def __init__(self,tip):
        self.tip=tip

if __name__ == '__main__':
    arena_residence = Bloc('nou')
    print("Arena Residence e un bloc ",arena_residence.tip)
    arena_residence.nr_etaje=4
    print("Are %d etaje" %arena_residence.nr_etaje)

    bloc_maria = Bloc("vechi")
    print(bloc_maria)


