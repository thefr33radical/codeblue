'''
Left view of a binary btree
T(C)=O(n+n-1)
'''

class btree(object):
    def __init__(self):
        self.left=None
        self.right=None
        self.val=0
        
def add_node(obj,left,right,val):
        obj.left=left
        obj.right=right
        obj.val=val


def preorder(obj):
    if(obj):
        if(obj.left is None and obj.right is None):
            print(obj.val)
        else:
            preorder(obj.left)
            preorder(obj.right)
        
    
    

def compute():
    obj=btree()
    obj.val=4
    
    obj1=btree()
    obj1.val=2  
    
    obj2=btree()
    obj2.val=5
    
    obj3=btree()
    obj3.val=6
    
    obj4=btree()
    obj4.val=7
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    
    maximum=0
    maximum=preorder(obj,maximum)
    print(maximum)

if __name__=="__main__":
    compute()
        
    