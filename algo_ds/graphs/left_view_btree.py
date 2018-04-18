'''
Left view of a binary btree

'''
from collections import defaultdict

class btree(object):
    def __init__(self):
        self.left=None
        self.right=None
        self.val=0
        
def add_edge(obj,left,right,val):
        obj.left=left
        obj.right=right
        obj.val=val


def left_view(obj):
    adj=defaultdict(list)
    q=[]
    level=0
    t=[]
    q.append([obj,level])
    t.append([obj,level])
    while(q):
        temp=q.pop(0)
        vertex=temp[0]
        
        lvl=temp[1]
        adj[lvl].append(temp[0].val)
        lvl+=1
        
        if(vertex.left):
            q.append([vertex.left,lvl])
            t.append([vertex.left,lvl])
        if(vertex.right):
            q.append([vertex.right,lvl])
            t.append([vertex.left,lvl])

    
    for i in adj:
       print(adj[i][0])
    
    
def compute():
    obj=btree()
    obj1=btree()
    obj2=btree()
    obj3=btree()
    obj4=btree()
    obj5=btree()
    add_edge(obj5,None, None,5)
    add_edge(obj4,None, None,4)
    add_edge(obj3,obj4, None,3)
    add_edge(obj2,obj3, None,2)
    add_edge(obj1,obj5, None,1)
    add_edge(obj,obj1, obj2,0)
    
    left_view(obj)
    ##print(i,obj.v[i])
if __name__=="__main__":
    compute()