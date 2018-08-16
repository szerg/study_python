#!/usr/local/bin/python3

"""Playing with formatting"""

x=3.5
y=54.67
# printeaza normal
print("coord carteziene sunt {0} si {1}".format(x, y))
# printeaza float cu 2 zecimale
print("coord carteziene sunt {:.2f} si {:.2f}".format(x, y))
# printeaza la logging 
print("rezultatele sunt x={:g} si y={:g}".format(x,y))
# printeaza procentual
print("{:g} inseamna {:.5%} din {:g}".format(x,x/y,y))
# printeaza cu un alt separator un numar mai mare
print("Universul are {:,} ani".format(16218268152812.3121))

a="Ana"
b='mere'
print('{} are {}'.format(a,b))
print("{:*^50}".format(a))
print("{:*>50}".format(a))
print("{:*<50}".format(a))