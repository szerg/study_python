import fileinput
import glob

filenames = glob.glob('./python3cookbook/*.csv')

# ia mai multe fisiere dar le citeste pe rand; are niste chestii cool gen tine numele fisierului , line_nr etc
# cel mai ok e faptul ca trateaza input redirects etc..gen ai putea scrie ls ..|./cap13.py si ia ca input ce vine din pipe
with fileinput.input(filenames) as f:
    for line in f:
        if f.isfirstline():
            print('\n* Reading {}'.format(f.filename()))
        print(line,end='')

# daca vrei sa iesi cu eroare
""" a=1
if a==1:
    raise SystemExit("Am iesit cu eroare!") """

print()
print('#'*50)

# pt parsare de args
import argparse
# fa un obiect pt parsare
argparser = argparse.ArgumentParser(description="Exercise file for cap13")
argparser.add_argument("url",help="URL to connect to")
argparser.add_argument("-v","--verbosity",help="verbosity option",action="store_true")
# parseaza efectiv; daca nu ai niciun argument e useful doar pentru a afisa un help message; ai automat optiunea -h, --help
args = argparser.parse_args()
if args.verbosity:
    print("Url is {}".format(args.url))
else:
    print(args.url)

print()
print('#'*50)

import getpass
user = getpass.getuser()
passwd = getpass.getpass()

print(passwd)

# rulare de comanda externa
import subprocess
ran = subprocess.run(['ls','-l'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(ran.returncode)
print(ran.args)
#print(ran.stderr.decode('utf-8'))
print(ran.stdout.decode('utf-8'))
# observ ca acum asta se face cu run

# daca vrei sa faci copii de fisiere ,arhive , mutare etc:
import shutil
# os.walk te ajuta sa cauti fisiere

print()
print('#'*50)

# daca vrei sa parsezi fisiere de configurare, sa zicem ini-uri, te folosesti de configparser; configparser poate mergeui si diverse fisiere
# daca vrei sa schimbi sys.path ar tb sa pui fisiere .pth intr-un director care exista deja in sys.path