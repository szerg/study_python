#!/usr/bin/python
# coding=utf-8

class ClasaDeTest:
    """Aici ar trebui sa fie documentatia pentru clasa asta."""
    # un fel de constructor
    def __init__(self,name,age):
        self.n=name
        self.a=age

    def setAge(self,newage):
        self.a = newage

if __name__ == '__main__':
    ClasaDeTestInstance = ClasaDeTest('Titi',14)
    print ClasaDeTestInstance.a, ClasaDeTestInstance.n
    print dir(ClasaDeTestInstance)
    # __doc__ contine mesajul ala intre 3 ghilimele
    print ClasaDeTestInstance.__doc__
    # nu trebuie definite inainte atributele clasei, o poti face direct in init
    # orice metoda trebuie sa aiba 'self' ca prim parametru
    ClasaDeTestInstance.setAge(15)
    ClasaDeTest.setAge(25)
    print ClasaDeTestInstance.a
    print ClasaDeTestInstance.setAge
    print ClasaDeTest.setAge
    # poti face o clasa goala, continand doar 'pass' si dupa instantiere sa poti sa adaugi atribute si metode...kind of weird
    # nu exista atribute/metode private dar exista posibilitatea de a le 'ascunde' folosind prefixul __, gen __age; asta e mai mult o conventie intrucat si aceste atribute pot fi modificate

