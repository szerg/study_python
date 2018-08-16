#!/usr/bin/python -tt

class Dog(object):
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name

class Human(object):
    def __format__(self,format):
        if format == 'cacat':
            return '$@#$#!~@~'
        return 'Unknown format!'

def main():
    # super simplu
    print 'Hello {}'.format('Johnny!')
    # pozitional
    print 'Salut {}! zice {}'.format('Gabi','Ioana')
    print 'Salut {1}! zice {0}'.format('Gabi','Ioana')
    # padding with a certain char
    print '{:_<10}'.format('test') # adauga dupa string caracterul de dupa :
    print '{:_^7}'.format('test') # centreaza
    print '{:_>10}'.format('test') # pune intainde de string caracterul de dupa :
    # padding with space
    print '{:10}'.format('spaces'),
    print 'test paddding on the same line'
    # truncate
    print '{:.5}'.format('bullshitter') # primele 5 caractere
    # combinat truncate cu padding
    print '{:10.7}'.format('motherfuckingshit'), # fa padding pana la 10chars dar trunchiaza de la 7 incolo
    print 'test padding'
    # formatare cu numere
    print '{:4d}'.format(12) # oadding in fata intului
    print '{:.4f}'.format(12.894590234) # float cu 4 zecimale
    print '{:04d}'.format(32) # padding cu 0
    print '{:10.4f}'.format(3.141592) # padding cu spatii, in total 10 caractere, precizie 4 zecimale (itiface  si round)
    print '{:+.2f}'.format(3.14) # semn si precizie cu 2 zecimale ca altfel o sa iti puna o precizie default
   
    # named placeholders
    dick = {'Titi': 'tigan borat', 'Carolina': 'vagaboanda'}
    print '{Carolina} s-a luat dupa un {Titi}'.format(**dick) # asta e un pic cam dubios
    print '{0[Titi]:s} s-a luat dupa o {0[Carolina]:s}'.format(dick)

    # de aici o poti lua pe aratura cu diverse...gen poti folosi diverse obiecte etc
    # pt exemplul asta am definit clasa aia Dog;
    # aici nu mai am un arg pozitional gen 0,1 ci trebuie folosit numele de obiect, in cazul nostru 'd'
    print '{d.name:s} is a fucking {d.breed:s}'.format(d=Dog('Chihuahua','Cuchi'))

    # formatare data
    import datetime
    print 'Today is {:%Y-%m-%d}'.format(datetime.datetime.now()) # ii dai un obiect data si iti formateaza afisarea lui

    # poti sa dai parametrizat acei format specifiers, ceva de genul:
    print '{:>{width}.{precision}f}'.format(3.145612334345,width=10,precision=5)
    # parametrizat tot; iti ia in ordine dupa primul argument al metodei format -a argument care reprezinta ce vrei sa fie formatat: cu ce sa iti faca padding,unde sa iti faca, care sa fie latimea afisajului, care sa fie precizia
    print '{:{}{}{}.{}f}'.format(3.34872389,'_','>',10,5)

    # ca sa iti faci un custom format treb definita metoda __format__ in cadrul clasei tale
    # facut clasa Human pt chestia asta care se foloseste de format specifier: 'cacat'
    print '{:cacat}'.format(Human())



if __name__ == '__main__':
    main()

