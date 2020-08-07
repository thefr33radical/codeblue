'''
kruskals algorithm for undirected weighted graph
Greedy Algorithm
T(C)=
'''

from collections import defaultdict
class wgraph(object):
    def __init__(self,v):
        self.adj=defaultdict(list)
        self.edges=[]
        self.v=v
    
    def add_edge(self,u,v,wt):
        self.adj[u].append([v,wt])
        self.adj[v].append([u,wt])
        self.edges.append([u,v,wt])
    
def myfunc(l):
    return l[2]
    
def kruskal(obj):
    obj.edges=sorted(obj.edges,key=myfunc)
    print(obj.edges)
if __name__=="__main__":
    # Driver co
    g = wgraph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
 
    kruskal(g)
    #g.KruskalMST()
        