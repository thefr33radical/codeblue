

'''
1.
declaring a list  N * N
mat=[[0]*N]*N
'''


'''
2.
Find the max key from a hash map
k=(max(dict.keys(), key=(lambda i:dict[i]))
print(max(ord('a'),ord('4')))
'''


'''
3.
Indexes:
Arr[int()] Usuually throws floatpoint error
sorting algorithms need exact indexes instead of size
'''


'''
4.
program body:

def compute():

if __name__=="__main__":
    compute()
'''


'''
5.
sorted(list,key=func)
https://www.programiz.com/python-programming/methods/built-in/sorted
'''


'''
6.
Unweighted Binary tree template:

class Tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        
def compute():
    obj=Tree(1)
    obj1=Tree(2)
    obj2=Tree(3)
    obj3=Tree(4)
    obj4=Tree(5)
    obj5=Tree(6)  
    obj6=Tree(7)  
            
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
'''

'''
7.
Sorting list of tuples/lists/custom objects 

https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/

'''

'''
8. Unweighted Graph template:

class graph(object):
    def __init__(self,vertex):
        self.adj=defaultdict(list)
        self.ver=vertex
        
def add_edge(obj,u,v):
        obj.adj[u].append(v)
        
def compute():
    obj=graph(5)
    
    add_edge(obj,0, 1)
    add_edge(obj,0, 2)
    add_edge(obj,0, 3)
    #add_edge(obj,1, 2)
    #add_edge(obj,2, 0)
   # add_edge(obj,2, 3)
    add_edge(obj,3, 4)
    add_edge(obj,4, 3)
    add_edge(obj,4, 8)
    add_edge(obj,2, 5)
    #add_edge(obj,0, 5)
    
   
   
if __name__=="__main__":
    compute()
'''