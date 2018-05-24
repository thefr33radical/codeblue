# -*- coding: utf-8 -*-

from collections import defaultdict

class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
        
def check_leaves(obj,s):
    q=[]
    q.append(obj.adj[s])
    print(q)
    while(q):
        temp=q.pop(0)
        isleaf=0
        
        for i in obj.adj[temp]:
           q.append(i)
           isleaf=1
           
        if isleaf==0:
            print(temp)
        
           
        
def compute():
    obj=graph(5)
    
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,3, 4)
    add_edge(obj,4, 7)
    add_edge(obj,4, 8)
    add_edge(obj,2, 5)
    #add_edge(obj,0, 5)
    check_leaves(obj,0)
    
if __name__=="__main__":
    compute()