import multiprocessing as p
import random as r
import string

q=p.Queue()

def func(s):
    print("Process : ",str(s)+" "+string.digits+string.ascii_lowercase)
    q.put(("Process : ",str(s)+string.digits+string.ascii_lowercase))
'''
d=[2,3,3,2,3]
#Process class
#z=[p.Process(target=func,args=(i)) for i in range(len(d))]
z = [p.Process(target=func, args=(x,)) for x in range(4)]

for i in z:
    i.start()
    
for i in z:
   i.join()
   
for i in z:
    print(q.get())
 '''   
###############################################################################
    #pool
'''
pool=p.Pool(processes=5)
output=[pool.apply(func,args=(x,)) for x in range(7)]   
for i in output:
    print(q.get())

''' 
pool=p.Pool(processes=5)
output=[pool.apply_async(func,args=(x,)) for x in range(7)]   
for i in output:
    print(q.get())


 

    