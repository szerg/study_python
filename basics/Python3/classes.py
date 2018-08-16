class Dog():
    """Creates a Dog class"""
    # asta e un atribut de clasa, e shared intre toate obiectele din clasa asta
    kind = 'caninus retardus'

    def __init__(self, age, weight):
        # Deci nu e necesara declararea variabilelor interne ale clasei inainte de initializare
        self.age = age
        self.weight = weight
    
    def new_kind(self,enhance):
        self.kind+=enhance

if __name__ == '__main__':
    myDog = Dog(7, 45)
    print("I have a dog of age {} and weight {}".format(myDog.age, myDog.weight))
    # atribute se pot asigna si dupa instantierea clasei
    myDog.hungry = True
    myDog.name = 'Fluffy'
    print("{} is hungry? {}".format(myDog.name, myDog.hungry))
    # interesant in sectiunea asta modificarile pe care le fac obiectului nu se reflecata clasei
    # si nici modificarile pe care le fac clasei nu se reflecta in obiectul anterior instantiat
    myDog.kind+=' magnificus'
    Dog.kind+=' mucificus'
    print("{} is {}".format(myDog.name,myDog.kind))
    print(Dog.kind)
    # dar modificarile de clasa se vad in obiectul instantiat apoi
    hisDog = Dog(2,15)
    hisDog.name = 'Rex'
    print("{} is {}".format(hisDog.name,hisDog.kind))
    # modificarile pe care le fac in alt obiect nu se vad in primul obiect la variabila asta de clasa
    hisDog.kind+=' blabla'
    print("{} is {}".format(myDog.name,myDog.kind))
    # modificari prin metode
    print("***Modificari prin metode***")
    myDog.new_kind(' brutalus')
    hisDog.new_kind(' alintatus')
    print(Dog.kind)
    print(myDog.kind)
    print(hisDog.kind)
    
