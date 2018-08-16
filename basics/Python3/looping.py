# index and value retrieval
fruits=['apple','orange','banana','grape','cherry']

for i,v in enumerate(fruits):
    print("Index is {} and value is {}".format(i,v))

# key,val retrieval
men={'tony':40,'steve':35,'clark':33}
for k,v in men.items():
    print(k)

# parcurge 2 liste in ac timp
q=['cine','ce','de ce']
a=['eu','fericire','pt ca poate merit']

for quest,ans in zip(q,a):
    print('{} bla bla {}'.format(quest,ans))

# mai putin elegant
for i in range(len(q)):
    print('{} bla bla {}'.format(q[i],a[i]))
# ar tb sa parcurgi o copie de lista si nu lista insasi


