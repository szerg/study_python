from collections import namedtuple
from collections import deque
import bisect
import array
import random

if __name__ == '__main__':
    # listcomp
    #a = [x for x in range(1000)]
    # print(a)
    # gencomp
    # asta iti creeaza un generator sa poti sa il incarci intr-un for
    b = (x for x in range(1000000))
    print(b)

    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # 1
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    # un anume nr de spatii ca header pt prima coloana plus centrari pet urmatoarele 2 coloane
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:  # 2
        if longitude <= 0:  # 3
            print(fmt.format(name, latitude, longitude))

    # namedtuple are o serie de proprietati misto
    City = namedtuple('City', 'name country pop, coord')
    tokio = City(*metro_areas[0])
    print(tokio.name)
    print(tokio._fields)
    print(tokio._asdict())

    # named slicing
    s = 'Ana are mere'
    name = slice(0, 3)
    action = slice(4, 7)
    print('Am extras din s numele: {!s} si actiunea: {!s}'.format(
        s[name], s[action]))

    # sorting
    fruits = ['mere', 'gutui', 'pere', 'portocale', 'banane']
    print(sorted(fruits))
    print(fruits)
    fruits.sort(key=len)
    print(fruits)

    # bisect
    # ideea ar fi sa cauti/inserezi undeva intr-un sequence ordonat: lista, array, collections.deque
    # deci initial sortezi, iei cu bisect indexul apoi inserezi propriu-zis..preferabil pastrand ordinea
    vegs = ['cartof', 'morcov', 'usturoi', 'leustean', 'varza', 'rosii']
    vegs.sort()
    print(vegs)
    bisect.insort_right(vegs, 'marar')
    print(vegs)

    #arrays
    # se comporta ca o lista insa poti pune in ele doar niste tipuri de date limitate: chars , ints , floats
    a = array.array('i',(random.choice(range(-127,128)) for x in range(10**2)))
    print(a[0],a[-1])
    # e mai rapid decat daca ai face o lista si in plus daca vrei sa scrii intr-un fisier are o 

    #queues
    # super fast la append si pop din capete
    # pot fi si circulare
    # sunt thread safe ceea ce inseamna ca la pop si append nu tb sa ai ceva sincronizare
    q = deque([1,2,3,4,5])
    q.popleft()
    print(q)
    
    

