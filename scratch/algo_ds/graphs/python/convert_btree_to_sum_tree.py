#Convert a given tree to its Sum Tree
# T(C)= O(n)

class Tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        

def sum_tree(obj):
    if(obj):
        cost=obj.val+sum_tree(obj.left)+sum_tree(obj.right)
        return cost
        
    else:
        return 0
        
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
    
    print("Sum of the tree is",sum_tree(obj))
    
if __name__=="__main__":
    compute()