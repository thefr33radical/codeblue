'''
Zig Zag Traversal for any type of tree

#Tree
T(C)=O(E+V)


1. Add edges into ajacency list
2. Convert into level ordered list.
3. Print list in reverse order if even

'''
from collections import defaultdict
class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def traverse(obj,src,x):
    q=[]
    q.append([src,0])
    levls=defaultdict(list)
    
    stck=[]
  
    '''  print(obj.adj)
    for i in range(len(obj.adj)):
        for j in obj.adj[i]:
            if(i%2!=0):
                stck.append(j)
            else:
                print(j)
        while(stck):
            print(stck.pop())
            
            '''
    
    
    while(q):
        temp=q.pop(0)
        v=temp[0]
        level=temp[1]
        levls[level].append(v)
        level+=1
        for i in obj.adj[v]:
           # print(i,level)
               
               #print(i)
               q.append([i,level])
                
            
                #t.append([i,level])
        
            
    print(levls)
    stck=[]
    for i in range(len(levls)):
        for j in levls[i]:
            if(i%2!=0):
                stck.append(j)
            else:
                print(j)
        while(stck):
            print(stck.pop())
    
   
        

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