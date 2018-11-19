import csv
from collections import namedtuple

with open('python3cookbook/stocks.csv') as f:
    csvfile = csv.reader(f)
    header = next(csvfile)
    # this allows you to create a tuple like object in care accesezi atribute pe baza de nume
    # nu mai folosesti chestii pozitionale
    row = namedtuple('Row',header)
    for line in csvfile:
        # aici expandezi tuplul citit in mai multe valori
        r = row(*line)
        print(r.Price)

##################################
import json
import pprint
# ai 2 metode pt dump/import de json in string: dumps /loads
# similar pt fisiere ai dump/load
dick = {'s':'admin','a':'dev','m':'qa'}
with open('dickfile','wt') as f:
    json.dump(dick,f)

with open('dickfile') as f:
    j = json.load(f)
    pprint.pprint(j)
##################################

import xml.etree.ElementTree

with open('python3cookbook/rss20.xml') as xf:
    
    parsed = xml.etree.ElementTree.ElementTree(xf)
    for i in parsed.iterfind('channel/item'):
        print(i.findtext('title'))

