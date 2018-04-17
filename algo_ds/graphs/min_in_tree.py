'''

Find maximum (or minimum) in Binary Tree


'''

class tree(object):
    def __init__(self):
        self.left=None
        self.right=None
        self.val=0
        
def add_node(obj,left,right,val):
        obj.left=left
        obj.right=right
        obj.val=val


def preorder(obj,maximum):
    if(obj):
        if(obj.val>maximum):
            maximum=obj.val
        maximum=preorder(obj.left,maximum)
        maximum=preorder(obj.right,maximum)
        
    return maximum
    

def compute():
    obj=tree()
    obj.val=4
    
    obj1=tree()
    obj1.val=2  
    
    obj2=tree()
    obj2.val=5
    
    obj3=tree()
    obj3.val=6
    
    obj4=tree()
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
        
    