class Dog:
    def __init__(self, name, age, size):
        self.name = name
        self.size = size
        self.age = age
    def __str__(self):
        return 'A dog named {} of age {} and {} size'.format(self.name, self.age,self.size)
    
    # forma generala recomandata pt o metoda de tipul acesta
    def __repr__(self):
        return '{}({},{},{})'.format(self.__class__.__name__, self.name, self.age, self.size)
    
if __name__ == "__main__":
    myDog = Dog('Rex',2,'medium')
    print(myDog) # <__main__.Dog object at 0x103c101d0>
    # daca pui __str__ iti printaeza ce returnezi in metoda aia

    print(repr(myDog))
    # daca apelezi repr iti printeaza ce e returnat de metoda __repr__

    # str , intern apeleaza repr, deci daca nu ar fi __str__ ti-ar printa ce returneaza __repr__
    # __str__ e mai degraba pt a face ceva inteligibil, human readable
    # __repr__ e pt o reprezentare clara a obiectului, de ex ar putea fi util daca vrei sa vezi cum a fost facut obiectul,
    # initializat si sa il faci din nou

    anotherDog = eval(repr(myDog))
    print(anotherDog)