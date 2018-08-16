class Animal:
    def __init__(self,animal_type):
        self.animal_type = animal_type


class Dog(Animal):

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        super().__init__('mammal')
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

a=Dog('titi')
b=Dog('rex')
a.add_trick('bark')
b.add_trick('jump')
# spre deosebire de classes.py unde creez acel string lucrurile aici variabila e afectata de metode
print(a.tricks)
# mostenire
print(a.animal_type)

