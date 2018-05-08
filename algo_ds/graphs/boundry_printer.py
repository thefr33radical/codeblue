'''
Boundry print a given binary tree:
T(C)=O(E+V)
Algorithm : BFS with edge case

'''
class tree(object):
    def __init__(self,v):
        self.left=None
        self.right=None
        self.val=v
        
def add_node(obj,left,right):
        obj.left=left
        obj.right=right
        
def isleaf(node):
    if(node):
        if(node.left or node.right):
            return 0
        else:
            return 1
        
def boundry(obj):
    q=[]
    q.append(obj)
    leftmost=0
    rightmost=0
    print(obj.val)
    while(q):
        leftmost=0
        v=q.pop(0)
       # print(v.val)
        if(isleaf(v)):
            print("leaf",v.val)
            continue
        else:
            if(v.left):
                if(leftmost==0 and not isleaf(v.left)):
                    print("left",v.left.val)                   
                    q.append(v.left)
                    leftmost=1
                else:
                    q.append(v.left)
                    
            if(v.right):
                if(leftmost==0 and not isleaf(v.right)):
                    print(v.right.val)
                    q.append(v.right)
                    leftmost=1
                else:
                    q.append(v.right)
        
            if(leftmost!=0 and not isleaf(q[len(q)-1])):
                print("right",q[len(q)-1].val)

        
def compute():
    obj=tree(1)
    obj1=tree(2)
    obj2=tree(3)
    obj3=tree(4)
    obj4=tree(5)
    obj5=tree(6)  
    obj6=tree(7)  
        
    
    obj.left=obj1
    obj.right=obj2
    
    obj1.left=obj3
    obj1.right=obj4
    
    obj2.left=obj5
    obj2.right=obj6
    #print(obj.val)
    boundry(obj)
    
if __name__=="__main__":
    compute()
    