'''
Program to check if a perfect binary tree or not
'''
leaflevel=None
class Tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right

def isleaf(obj):
    if(obj.left is None and obj.right is None):
        return True
    else:
        return False
def check_node(obj):
    if(obj.left is not None and obj.right is not None):
        return True
    else:
        return False
                
def check_perfect_btree(obj,level,leaflevel):
    level+=1 
    if(isleaf(obj))  :
        if leaflevel is None:
            leaflevel= level
            return True
        else:
            if level == leaflevel:
                return True
            else:
                return False
    else:
        if(check_node(obj)):
            return check_perfect_btree(obj.left,level,leaflevel) and check_perfect_btree(obj.right,level,leaflevel)
        else:
            return False
        
def compute():
    obj=Tree(1)
    obj1=Tree(2)
    obj2=Tree(3)
    obj3=Tree(4)
    obj4=Tree(5)
    obj5=Tree(6)  
    obj6=Tree(7)  
    obj7=Tree(8)     
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
    obj4.right=obj7
    
    print(" Is the given tree is Perfect binary Tree :",check_perfect_btree(obj,0,None))

if __name__=="__main__":
    compute()