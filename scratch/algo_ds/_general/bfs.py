from collections import defaultdict

class graph(object):
    def __init__(self):
        self.v=defaultdict(list)
        
def add_edge(obj,src,dest):
    obj.v[src].append(dest)
    pass
        
def bfs(obj):
    q=[]
    visited=[False]*(len(obj.v))
    
    src=2
    dest=5
    
    visited[0]=True
    q.append(src)
    
    
    t=[]
    t.append(str(src)+"->")
    while(q):
        cur_vertex=q.pop(0)
        if(cur_vertex==dest):
            break
        for i in obj.v[cur_vertex]:
            if(visited[i]==False):
                t.append(str(i)+"->")
                temp_vertex=i
                visited[i]=True
                q.append(temp_vertex)
    
    print(t)

def compute():
    obj=graph()
    
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,1, 2)
    add_edge(obj,2, 0)
    add_edge(obj,2, 3)
    add_edge(obj,3, 3)
    add_edge(obj,4, 3)
    add_edge(obj,2, 4)
    
    bfs(obj)
    ##print(i,obj.v[i])
if __name__=="__main__":
    compute()