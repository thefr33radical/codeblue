'''
DFS for any type of tree

#Tree
T(C)=O(E+V)


1. Add edges into ajacency list
2. Convert into level ordered list. (recursion/iteration)

'''
from collections import defaultdict
class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def dfs(adj,src,l,level):
    
        
    for i in adj[src]:
        l[level].append(i)
        dfs(adj,i,l,level+1)
        print(i)

def traverse(obj,src,x):
    
    l=defaultdict(list)
    dfs(obj.adj,0,l,0)
        
    print(l)   

def compute():
    obj=graph(5)
    level_count=2
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    add_edge(obj,1, 6)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,3, 4)
    add_edge(obj,4, 7)
    add_edge(obj,2, 5)
    add_edge(obj,5, 8)
    add_edge(obj,6, 9)
    #add_edge(obj,0, 5)
    
   # print((obj.ver))
    traverse(obj,0,level_count)
    ##print(i,obj.v[i])
if __name__=="__main__":
    compute()