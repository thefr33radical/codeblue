#kahns algorithm : T(C)=O(V+E)


from collections import defaultdict
class graph(object):
    def __init__(self,v):
        self.indegree=[0]*v
        self.adj=defaultdict(list)
        
def add_edge(obj,src,dest):
    obj.indegree[dest]+=1
    obj.adj[src].append(dest)
    
def topological_sort(obj):
   # a=(obj.indegree)
    #print(a)
    
    #visited=[False]*(len(obj.adj)+1)
    #src=obj.indegree.index(min(obj.indegree))
    #print(src)
    q=[]
    for i in range(len(obj.indegree)):
        if(obj.indegree[i]==0):
            q.append(i)
    
    
   # q.append(src)
   # visited[src]=True
    cnt=0
    v=[]
    while(q):
        cur_vertex=q.pop(0)
        print(cur_vertex)
        v.append(cur_vertex)
        for i in obj.adj[cur_vertex]:
            
                obj.indegree[i]-=1
                
                if(obj.indegree[i]==0):
                    temp=i
                    q.append(temp)
        print(obj.indegree)
                
                
        cnt+=1
    if(cnt==len(obj.adj)):
            print(v)
    else:
        print("Cycle Exists")
            
    
    


def compute():
    g=graph(6)
    add_edge(g,5, 2);
    add_edge(g,5, 0);
    add_edge(g,4, 0);
    add_edge(g,4, 1);
    add_edge(g,2, 3);
    add_edge(g,3, 1);
    
    topological_sort(g)    
    #for i in g.indegree:
       # print(i,g.indegree[i])


if __name__=="__main__":
    compute()
    