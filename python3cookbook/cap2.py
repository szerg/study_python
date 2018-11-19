# re.split is better than split if delimiters are inconsistent

junk_string = 'jhsdasd,dgffsa 234jhj; 23hjfdj     sdas:QW'

import re
print(re.split(r'[,;\s:]\s*',junk_string))

# startswith, endswith pt simple matching la inceput si sfarsit; au nevoie de tuples ca input

websites = [ 'https://python.org','https://mail.google.com','smb://http://cacat.ro']
print([website for website in websites if website.startswith(('https://','http://'))])

# cand ai mai multe cautari e bine sa faci un compile al regexului inainte pt optimizare
# niste metode utile din pachetul re ar fi match, care cauta la inc de string , findall care cauta in tot stringul si return o lista cu matchurile
# text replacement : str.replace si re.sub daca vrei sa folosesti ceva mai complicat
# daca vrei sa concatenezi stringuri dintr-un iterable the best way is join; pt 2 3 stringuri e ok si +

# text operations on bytestrings
s = b'Hello'
# ai grija ca asta printeaza un integer, nu litera
print(s[0])
print(s.startswith(b'H'))
# in principiu merg slicing , diverse operatii de starts endswith iterare etc doar ca treb sa pui b''
print(s.decode('utf-8'))
# in principiu ar fi bine sa folosesti stringuri normale , nu byte strings chiar daca sunt slightly faster
