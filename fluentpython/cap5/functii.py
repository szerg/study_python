import random
# functiile in python sunt first-class objects; adica:
# pot fi asignate unei variabile, returnate, date ca argument la alte functii

def factorial(n):
    '''Mizerie care returneaza factorialul lui n; n trebuie sa fie un int'''
    # if else intr-o linie
    return 1 if n < 2 else n*factorial(n-1)

def variables(mandatory_first,*args,**kwargs):
    print(mandatory_first)
    for arg in args:
        print('From arg: {}'.format(arg))
    for k,v in kwargs.items():
        print('From kwargs: nume={},valoare={}'.format(k,v))


class Car:
    owners = ['A','B','C','D']
    def __init__(self, owner):
        self.owner = owner
    
    def change_owner(self):
        self.owner=self.owners[random.randint(0,len(self.owners)-1)]
    
    def __call__(self):
        return self.change_owner()

if __name__ == '__main__':
    print(factorial(5))
    print(factorial)
    # ca sa vezi docstringul
    print(factorial.__doc__)

    # map, filter, reduce sunt high order functions , adica primest ca argument o functie sau returneaza la randul lor o functie
    # nu mai sunt chiar asa importante dupa introducere de listcomp si dictcomp
    # map,filter returneaza generatori

    # functii lambda = functii anonime: sunt o forma de functii foarte simple , cu putina logica in ele pt ca nu poti face
    # looping sau asignari si sunt utilizate in special ca argumente la diverse functii
    # ex
    fruits = ['mere','pere','gutui','banane','portocale']
    print(sorted(fruits,key=lambda x: x[::-1]))

    # cand pui o functie __call__ in interiorul unei clase , obiectele create pot fi tratate ca functii
    dealer_car = Car('Pat')
    print(dealer_car.owner)
    dealer_car.change_owner()
    print(dealer_car.owner)
    # call-ul de mai jos va apela __call__ care va face exact ce face apelul de mai sus de change_owner; __call__ practic implementeaza ()
    dealer_car()
    print(dealer_car.owner)

    # toate atributele unui obiect  sunt stocate in __dict__
    # care e faza cu *args si **kwargs? 
    # pai numele alea args,kwargs nu sunt obligatorii, dar * si ** sunt; ideea e sa poti apela o functie cu un nr variabil de parametri
    variables('Ana','are','mere',special='para')
    variables('Ana',*['are','n-are','mananca'],special='para')
    variables('Ana','are','mere',special='para',gustos='musca')
    # trebuie respectata ordinea arg din semnatura functiei dar in principiu cu semnatura aia cu args  si kwargs
    # poti da orice lista de parametri; chestia asta e utila daca de ex se schimba cumva implementarea unei clase pe care o mostenesti
    # si nu vrei sa iti bati capul cu analiza parametrilor de __init__ si ii dai self,*args,**kwargs