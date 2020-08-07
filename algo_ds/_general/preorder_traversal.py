
#Preorder traversal for binary tree
'''class node:
    def __init__(self):
        self.val=0
        self.left=None
        self.right=None
        
    def add_node_left(self,val):
        self.left=node()
        self.val=val
    
    def add_node_right(self,val):
        self.right=node()
        self.val=val
        
   
        
def compute():
    t=node()
    t.add_node_left(10)
    t.add_node_right(20)
   
    root=t
    t.left=node()
    t.add_node_left(30)
    t.right=node()
    t.add_node_right(40)
    
    t=root
    t.left=node()
    t.add_node_left(50)
    t.right=node()
    t.add_node_right(60)
    
    root.printer(t)
    
    pass


if __name__=="__main__":
    compute()
    
    
    '''
    
class node:
    def __init__(self):
        self.val=0
        self.left=None
        self.right=None
        
        
def pre_order(node):
        temp=node
        print(temp.val)
        if(temp.left):
            print("left")
            pre_order(temp.left)
        if(temp.right):
            print("right")
            pre_order(temp.right)
            

def compute():
    
    root=node()
    root.val=1
    
    temp=node()
    temp.val=2
    root.left=temp
    
    temp2=node()
    temp2.val=3
    root.right=temp2
    
    temp3=node()
    temp3.val=4
    temp.left=temp3
    
    temp4=node()
    temp4.val=5
    temp.right=temp4   
        
    pre_order(root)

if __name__=="__main__":
    compute()
    