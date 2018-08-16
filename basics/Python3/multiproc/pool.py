# aparent maparea aia pe multiproc e mult mai ineficienta decat map propriu-zis
from multiprocessing import pool
from time import time

def f(x):
    return x*x

if __name__ == '__main__':
    start = time()
    with pool.Pool(10) as p:
        print(p.map(f, list(range(10))))
    print("Pool multiprocessing took {}".format(time()-start))

    start = time()
    print(list(map(f,list(range(10)))))
    print("Single processing took {}".format(time()-start))