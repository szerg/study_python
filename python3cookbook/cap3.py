import numpy

# e cel mai bun atunci cand vrei sa calculezi chestii pe un array de valori, sau vrei sa faci ceva cu ele 
an = numpy.array([1,2,3,4])
bn = numpy.array([10,20,30,40])
print(an*bn)
print(numpy.sqrt(an))

# prea vast pt doar cateva ex. ideea e ca daca treb facute diverse calcule si cu matrici polinoame etc, libraria asta is the way to go

# pt a folosi chestii pseudorandom e buna libraria random; a nu se folosi in crypto 
import random
print(random.randint(0,100))
a = [23,2,23,2,32,4,5346,35463]
print(random.choice(a))

# pt manipulari simple de date foloseste datetime
import date
# pt manipulari mai complexe foloseste dateutil; treb sa instalezi python-dateutil