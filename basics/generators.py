# se comporta ca o functie;
# trebuie neaparat sa aiba un yield
# in cazul de fata in loc sa itereze prin toate orasele la fiecare call all next se va returna unul din orase

def get_city():
    cities = ['Lon','Buc','Par','Bej','Mad']
    for i in cities:
        yield i


c1 = get_city()
print(next(c1))
print(next(c1))

# acum ideea e sa ai un lazy evaluation si sa faci economie de memorie
# in ex de mai sus, cred ca generatorul nici macar nu e folosit corect; un ex mai corect ar fi urmatorul

def large_list_of_nr(n):
    if n < 1_000_000:
        return []
    import random
    while n >0:
        yield random.randint(100,1000)
        n-=1

# xl_list = large_list_of_nr(5)
# for el in xl_list:
#     print(el)

xxl_list = large_list_of_nr(2_000_000_000)
for el in xxl_list:
    print(el)

# acuma sa zicem ca am face o lista intreaga mare fara genrator
import random
l = []

for i in range(2_000_000_000):
    l.append(random.randint(100,1000))


