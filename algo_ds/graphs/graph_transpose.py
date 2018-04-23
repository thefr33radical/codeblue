'''
Transpose of a graph
#Directed unweighted graph
T(C)=O(E)
'''

from collections import defaultdict
class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.transpose=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        obj.transpose[v].append(u)
def count(obj):
    print(obj.adj)
    print("--")
    print(obj.transpose)
    
            
        

def compute():
    obj=graph(5)
    
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,3, 4)
    add_edge(obj,4, 3)
    add_edge(obj,4, 8)
    add_edge(obj,2, 5)
    #add_edge(obj,0, 5)
    
    print((obj.ver))
    count(obj)
    ##print(i,obj.v[i])
if __name__=="__main__":
    compute()