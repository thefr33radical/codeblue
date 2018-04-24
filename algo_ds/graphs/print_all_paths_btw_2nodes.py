'''
Print all paths beteeen 2 nodes
T(C)=Exponential
Algorithm : DFS for each path
'''
from collections import defaultdict

class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex

def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def dfs(obj,vertex,dest,path,visit):
    if(vertex==dest):
        visit[dest]=True
        print(path)
       # print("\n")
        return
    if(visit[vertex]==False):
        visit[vertex]=True
        for i in obj.adj[vertex]:
            dfs(obj,i,dest,path+"->"+str(i),visit)
        
        
def compute():
    obj=graph(4)
    src=0
    dest=0
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,2,0)
    add_edge(obj,2,1)
    add_edge(obj,1,3)
    
    path=str(src)
    visit=[False]*4
    for i in obj.adj[src]:
        
        dfs(obj,i,dest,path+"->"+str(i),visit)
        visit=[False]*4
        #Dfs visits each node once, in order to find all paths between 2 nodes make visit array as false
   
   
if __name__=="__main__":
    compute()