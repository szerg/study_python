#!/usr/bin/python
 # -*- coding: utf-8 -*-

euro = "Є"
pound = "£"

print "Symbols for pounds %s and euros %s" % (pound,euro)

print "Again pounds",unichr(163)

# Deci ideea e ca daca se folosesc caractere speciale trebuie pus headerul de sub shebang. ord e fct care intoarce nr corespunzator codarii unicode/ascii/latin-1 in timp ce unichr/chr intoarce simbolul asociat numarului.
# decuadskjasnfsaldklasdkffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

# din momentul iun care pui ala cu textwidth va face wrap around la toate
# mizeriile si ce e mai cul e ca nu iti va taia cuvintele. de exemplu pentru
# textul:
# saddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
# nu a taiat nimic cu toate ca e f mare

print "acum testez mizeria asta cu colorcolumn , sunt curios ce face ar
trebuiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
sa faca highlight pe randurile mai mari ca 80"

print "ana are asdkljfcsaldkc oasj alk ;ak; klasod j;sak ;askd jka;sdk
sa;kdfas;kd ksdaf lkasdf; ak;kl  asdf asdf asdjf naslkdjf skdfdfad asdkfdskajdk"
