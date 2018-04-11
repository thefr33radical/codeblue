
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
        
    def printer(self,node):
        temp=node
        print(temp.val)
        if(temp.left):
            self.printer(temp.left)
        if(temp.right):
            self.printer(temp.right)
        
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