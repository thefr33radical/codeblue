
class node:
    def __init__(self):
        self.val=0
        self.left=None
        self.right=None
        
def post_order(node):
    temp=node
    
    if(temp.left):
            print("left")
            post_order(temp.left)
            
    if(temp.right):
            print("right")
            post_order(temp.right)
    print(temp.val)

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
    
    
    
    post_order(root)

    
                
            