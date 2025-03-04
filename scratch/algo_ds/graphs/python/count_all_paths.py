'''
Count paths beteeen 2 nodes
T(C)=Exponential
Algorithm : DFS for each path
'''
from collections import defaultdict

class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        self.count=0
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def dfs(obj,vertex,dest,visit):
    if(vertex==dest):
        visit[dest]=True
        obj.count+=1
       # print("\n")
        return
    if(visit[vertex]==False):
        visit[vertex]=True
        for i in obj.adj[vertex]:
            dfs(obj,i,dest,visit)
        
        
def compute():
    obj=graph(4)
    src=2
    dest=3
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,2,0)
    add_edge(obj,2,1)
    add_edge(obj,1,3)
    
    
    visit=[False]*4
    for i in obj.adj[src]:
        
        dfs(obj,i,dest,visit)
        visit=[False]*4
    print(obj.count)
        #Dfs visits each node once, in order to find all paths between 2 nodes make visit array as false
   
  
if __name__=="__main__":
    compute()