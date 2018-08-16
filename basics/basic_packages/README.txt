##  exemplu simplu despre cum se folosesc pachetele in python

1. Cazul 'graphics':
    in directorul graphics trebuie sa existe fisierul __init__.py ca sa poti sa faci import, asta ii spune python ca trebuie sa trateze directorul ca pe un pachet
    nu importa *, best practice, adica nu face : from graphics import *
    daca totusi faci asta, in __init__.py trebuie definita variabila __all__ care contine numele modulelor ce vrei sa fie importate
    cel mai bine este: from graphics import splashscreen sau import graphics.splashscreen
    atentie la path-ul catre chestiile din modul pe care vrei sa le folosesti; e mai bine sa folosesti un path absolut
    
    
