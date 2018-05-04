
class tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        
def find_path(obj,val,q):
    found=0
    if(obj is None):
        
        return 0
    if(obj.val==val):
        return 1
    q.append(obj)
    
    found=find_path(obj.left,val,q)
    if(found==0):
        found=find_path(obj.right,val,q)
    else:
        return 1
        
    if(found==0):
        q.pop()
        return 0
        
    else:
        return 1
    
        
def lca(obj,val1,val):
    q1=[]
    q2=[]
    found1=0
    found2=0
    
    found1=find_path(obj,val1,q1)
    found2=find_path(obj,val,q2)
    '''
    for i in q1:
        print(i.val)
    print('---')
    for i in q2:
        print(i.val)
        
        '''
        
    while(len(q1)>0 and len(q2)>0):
        
            if(q1[0]==q2[0]):
                temp=q1.pop(0)
                q2.pop(0)
            else:
                break
            
    print(temp.val)

def compute():
    obj=tree(0)
    obj1=tree(1)
    obj2=tree(2)
    obj3=tree(3)
    obj4=tree(4)
    obj5=tree(5)  
    obj6=tree(6) 
    
    obj7=tree(7)
    obj8=tree(8)  
    obj9=tree(9)  
    
    obj10=tree(10)
    obj11=tree(11)  
    obj12=tree(12)  
        
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
    
    
    obj5.right=obj7
    obj7.left=obj8
    obj8.left=obj9
    obj8.right=obj10
    obj10.left=obj11
    obj11.right=obj12
    
    lca(obj,9,12)
    
if __name__=="__main__":
    compute()