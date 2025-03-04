'''
https://www.geeksforgeeks.org/count-number-nodes-given-level-using-bfs/

#Tree
T(C)=O(E+V)

'''
from collections import defaultdict
class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def count(obj,src,x):
    q=[]
    q.append([src,0])
    t=[]
    t.append([src,0])
    while(q):
        temp=q.pop(0)
        v=temp[0]
        level=temp[1]
        level+=1
        
        for i in obj.adj[v]:
            q.append([i,level])
            t.append([i,level])
    print(t)
    
    count=0
    for i in t:
        if(i[1]==x):
            count+=1
    print(count)
            
        

def compute():
    obj=graph(5)
    level_count=2
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,3, 4)
    add_edge(obj,4, 8)
    add_edge(obj,2, 5)
    #add_edge(obj,0, 5)
    
    print((obj.ver))
    count(obj,0,level_count)
    ##print(i,obj.v[i])
if __name__=="__main__":
    compute()