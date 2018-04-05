
from collections import defaultdict
 
class Graph(object):
    def __init__(self,u,v):
        self.src=u
        self.dest=v
        self.list=[]

def compute():
    
    d=defaultdict(list)
    l=[1,2,3,4,5,6]
    
    for i in range(16):
        if(i in l):
            d[i].append(i)
            d[i].append(i*2)
        else:
            pass
        
    print(d)
        
    

if __name__=="__main__":
    compute()