# Check if a given Binary Tree is SumTree
#T(C)= O(n)


class Tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        
def check_sum_tree(obj):
    if(obj):
        print(obj.val)
        if obj.left is None and obj.right is None:
            return obj.val
        
        if obj.val == (check_sum_tree(obj.left) + check_sum_tree(obj.right)):
            print("--",obj.val)
            return obj.val
        else:
            return -1
        
               
    else:
        return 0
        
def compute():
    obj=Tree(22)
    obj1=Tree(9)
    obj2=Tree(13)
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
    

    if (check_sum_tree(obj)==obj.val):
        print(" This is a sum tree ",check_sum_tree(obj))
    else:
        print(" Not a sum tree",check_sum_tree(obj))


if __name__=="__main__":
    compute()