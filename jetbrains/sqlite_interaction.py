import sqlite3
import pprint

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute('select * from card;')
#cur.execute('select number,pin from card where number = "4000003051194591" and pin = "8961";')
pprint.pprint(cur.fetchall())

