import os
import threading
import time

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def fact(n):
    if n<0:
        return print("Оnly positive number")
    elif n==0:
        return 1
    else:
        return n*fact(n-1)

with ThreadPoolExecutor() as executor:
    start1 = time.time()
    f1=executor.submit(fact, 900)
    f2=executor.submit(fact, 800)
    f3=executor.submit(fact, 600)
    f1.result()
    f2.result()
    f3.result()
    finish1 = time.time()
    t1 = finish1 - start1

if __name__ == '__main__':
    start2 = time.time()
    with ProcessPoolExecutor() as executor:
        res=[]
        res=executor.map(fact, [900, 800, 600])
    finish2=time.time()
    t2=finish2-start2

    if t1>t2:
        print("ThreadPoolExecutor() is better of ProcessPoolExecutor()")
    elif t1<t2:
        print("ProcessPoolExecutor() is better of ThreadPoolExecutor()")
    else:
        print("ProcessPoolExecutor() equally ThreadPoolExecutor()")

