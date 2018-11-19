# ignoring values

numbers = [4,2,5,6,79,123]
# ignore first and last
# also *something creates a list , nr arbitrar de elemente
_,*vars_of_interest,_ = numbers

print(vars_of_interest)

# using dequeue for fast pops,popleft etc
from collections import deque

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)
print(d[1])

# cele mai mari/mici n chestii; a se folosi pt un nr n relativ mic
# priority queues
import heapq
n = [123,1323143,4534,121546,676867,1782,27834,1,6,4,432,2]
h = heapq.nlargest(3,n)
print(h, type(h))

# defaultdict e folosit in general ca sa mapezi o cheie la mai multe valori sau sa faci ceva procesare pt valorile unei chei
from collections import defaultdict
dick = defaultdict(int)
l =[('a',1),('b',2),('a',1),('c',3)]
for k,v in l:
    dick[k]+=v
print(dick)

# pentru ordinea dintr-un dictionar poti folosi OrderedDict
# daca vrei sa obtii un dictionar cu elementele comune/disjuncte etc a 2 dictionare poti folosi operatii de seturi: &,-

# daca vrei sa numeri aparitiile unui obiect intr-un dictionar cel mai util e sa folosesti collections.Counter
from collections import Counter

c = Counter('abramburica')
# asta iti va printa un dictionar avand literele chei si de cate ori apare litera respectiva valori
print(c)

# posibilitatea de a grupa date in fctie de o valoare; this could prove useful
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key = lambda x: x['date'])
for ts, items in groupby(rows,lambda x : x['date']):
    print(ts)
    for i in items:
        print(i)


# list,dict comprehensions are generally faster