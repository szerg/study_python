import gzip
import os

# with open(r'C:\Users\sneculai\Projects\study_python\python3cookbook\arhiva.txt','rt') as f:
#     print(f.read())

with gzip.open(r'C:\Users\sneculai\Projects\study_python\python3cookbook\arhiva.txt.gz') as arhiva:
    print(arhiva.read().decode('utf-8'))

# os.path e useful pt manipularea de pathuri de fisiere , sa iei extensia etc
arhiva_path = r'C:\Users\sneculai\Projects\study_python\python3cookbook\arhiva.txt.gz'
print(os.path.basename(arhiva_path))
print(os.path.abspath(arhiva_path))
print(os.path.join('tmp','data'))
# os.listdir os.stat , os.mtime

# lower level of working with temp files
import tempfile
fd,fname = tempfile.mkstemp(prefix='rap',dir='.')
print(fd,fname)
os.close(fd)
os.remove(fname)

# better way; se ocupa automat de close 
with tempfile.NamedTemporaryFile() as fuck:
    print(fuck.name)

