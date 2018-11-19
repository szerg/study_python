import pprint
from collections import defaultdict
from collections import OrderedDict, Counter


if __name__ == '__main__':
    # create dictionaries
    d = dict(a=1, b=2, c=3)
    pprint.pprint(d)
    d1 = {'x': 1, 'y': 2}
    pprint.pprint(d1)

    # e misto ca poti sa faci unul din zip
    dicks = dict(zip(('S', 'A', 'T'), (15, 'unknown', 3)))
    # zip returneaza o lista mergeuita element cu element
    pprint.pprint(dicks)

    # dict comprehensions, similare cu list comprehensions
    names = ['B', 'S', 'V', 'A']
    jobs = ['qa', 'dev', 'sec', 'manager']
    positions = {name: job for (name, job) in zip(names, jobs)}
    pprint.pprint(positions)
    # in principiu cand vrei sa iei o cheie dintr-un dictionar folosesti d[k], daca nu e acolo primesti KeyError
    # daca vrei cumva sa tratezi altfel asta poti sa folosesti d.get(k,defaultvalue)
    # e o metoda smechera de get/set pt dictionare setdefault:
    new_dick = dicks.setdefault('B', 20)
    # nu era cheia in dict si a pus-o
    pprint.pprint(dicks)
    # ti-a si returnat valoarea
    print(new_dick)

    # defaultdict e interesant prin prisma faptului ca iti va returna o valoare de tipul definit la inceput la crearea dictionarului
    # pentru o cheie care nu exista in dictionar
    cities = defaultdict(list)
    cities.update({'Tokio': 1000000, 'NY': 5000000})
    print(cities)
    # asta mai jos iti printeaza o lista goala pt ca asta i-ai dat ca default la initializare;
    print(cities['Mumbai'])

    # counter e misto ca si implementare pt numarat chestii
    c = Counter('jkasdlajd;ajlwexlckajz;xlsa')
    print(c)
    print(c.most_common(2))

    # OrderedDict e pt a mentine o ordine a cheilor in ordinea adaugarii

    # sets
    # constructia de seturi e mai eficienta sa o faci fara constructori, dar daca setul e gol treb folosit constructorul set()
    s = set()
    s.add(1)
    sn={1,2,3,3,4,5,6,7,7}
    print(sn)
    print(s&sn)