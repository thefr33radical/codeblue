#Symmetric Tree

class tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        

        
def check_symmetry(obj1,obj2):
    if(obj1 is None and obj2 is None):
        return 1
    
    if(obj1 and obj2):
        #print("left",obj1.val,"right",obj2.val)
        if(obj1.val==obj2.val):
            #print("#left",obj1.val,"#right",obj2.val)
            x=check_symmetry(obj1.left,obj2.right) 
            y= check_symmetry(obj1.right,obj2.left)
            z=x and y
            print(x,y,z,"Exit : left",obj1.val,"right",obj2.val)
            return z
    #print("Exit : left",obj1.val,"right",obj2.val) 
    if(obj1):
        print("Exit mismatch",obj1.val)
    if(obj2):
        print("Exit mismatch",obj2.val)
    return -1
    
            
  
        
    
        
def compute():
    obj=tree(1)
    obj1=tree(2)
    
    
    obj2=tree(2)
    obj3=tree(3)
    obj4=tree(4)
    obj5=tree(4)  
    obj6=tree(3)  
    
    obj7=tree(10)
    obj8=tree(10)
    obj9=tree(41)  
    obj10=tree(41)  
    obj11=tree(0)  
        
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
    
    obj3.left=obj7
    obj6.right=obj8
    
    obj7.left=obj9
    obj8.right=obj10
    #obj8.left=obj11
    print(check_symmetry(obj1,obj2))

        
if __name__=="__main__":
    compute()
        