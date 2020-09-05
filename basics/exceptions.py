#!/usr/bin/python
# coding=utf-8

if __name__ == '__main__':
    while True:
        try:
            x = int(input("Please enter a number:"))
            break
        except(ValueError):
            print("Please provide a number!")
    try:
        print(10/0)
    except(ZeroDivisionError):
        # eroarea nu va fi afisata ci va fi capturata aici
        print("Divide by zero exception has occured")
    finally:
        # clauza asta in general e folosita ca sa eliberezi resurse indiferent daca try-ul a avut succes sau nu
        print("This always prints at the exist of try block")
