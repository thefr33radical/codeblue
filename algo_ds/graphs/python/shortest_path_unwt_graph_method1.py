'''
Shortest path in a unweighted graph
BFS
T(C)=O(V+E)

'''
from collections import defaultdict

class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def shortest_path(obj,src,dest):
    visit=[False]*obj.ver
    min_dist=[0]*obj.ver
    path=defaultdict(list)
    q=[]
    q.append(src)
   # dist=0
    visit[src]=True
    min_dist[src]=0
    while(q):
        v=q.pop(0)
        
        print(v,min_dist)
        for i in obj.adj[v]:
            if(visit[i] is False):
                q.append(i)
                visit[i]=True
                min_dist[i]=1+min_dist[v]
                path[i].append(str(v)+"-->"+str(i))
                
# print(min_dist,path)

def compute():
    adj=graph(8)
    
    add_edge(adj, 0, 1);
    add_edge(adj, 0, 3);
    add_edge(adj, 1, 2);
    add_edge(adj, 3, 4);
    add_edge(adj, 3, 7);
    add_edge(adj, 4, 5);
    add_edge(adj, 4, 6);
    add_edge(adj, 4, 7);
    add_edge(adj, 5, 6);
    add_edge(adj, 6, 7);
    source = 0
    dest = 7
    ##print(i,obj.v[i])
    shortest_path(adj,source,dest)
if __name__=="__main__":
    compute()