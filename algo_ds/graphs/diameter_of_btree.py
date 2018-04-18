'''
Diameter of Btree
T(C)=O(V+E)
'''
class tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        
        
def height(obj):
    if(obj):
        if(obj.left is None and obj.right is None):
            #print(0,obj.val)
            return 0
    
        else:
            x=(1+max(height(obj.left),height(obj.right)))
            #print(x,obj.val)
            return x
    else:
        return 0
        
def diameter(obj):
    if(obj):
        
        rdm=diameter(obj.right)
        ldm=diameter(obj.left)
        
        lht=height(obj.left)
        rht=height(obj.right)
        
        x= max(lht+rht+1,max(ldm,rdm))
        print(obj.val,x)
        return x
    else:
        return 0
        
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
        
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
    
    obj6.left=obj7
    obj7.left=obj8
    #print(height(obj))
    print(diameter(obj))
    
if __name__=="__main__":
    compute()