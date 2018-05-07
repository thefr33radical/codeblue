import multiprocessing as p
import random as r
import string

def func(s):
    print("Process : ",str(s)+string.digits+string.ascii_lowercase)

d=[2,3,3,2,3]
#z=[p.Process(target=func,args=(i)) for i in range(len(d))]
z = [p.Process(target=func, args=(x,)) for x in range(4)]

for i in z:
    i.start()