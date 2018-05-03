class tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        
def find(obj,val,stck1):
    
    find(obj.left,val)
    pass
        
def lca(obj,parent,val1,val):
    stck1=[]
    stck2=[]
    
    find(obj.left,val1,stck1.append(obj))
    
    
   
    
        
    
        
   return parent
        
def compute():
    obj=tree(1)
    obj1=tree(2)
    obj2=tree(3)
    obj3=tree(4)
    obj4=tree(5)
    obj5=tree(6)  
    obj6=tree(7)  
        
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
