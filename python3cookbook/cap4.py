import itertools
# pachetul de mai sus e important pt dverse chestii , gen grupari, permutari

#ex
sir = ('a','b','c','d','e')
for i in itertools.permutations(sir,2):
    print(i)

for i in itertools.islice(sir,2):
    print(i)


# cand vrei sa treci printr-o secventa si sa tii si indexul, enumerate() is the best