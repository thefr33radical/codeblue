import random
class node(object):
    def __init__(self,value,ptr):
        self.val=value
        self.next=None


def compute():
    head=node(4,None)
    g=[node(0,None)]*10
    for i in range(len(g)-1):
        g[i].val=random.randint(1,500)
        
        g[i].next=g[i+1]
        #print(g[i].val)
    g[len(g)-1].next=None
    
    
    head.next=g[0]
    
    temp=g[0]
    
    while(temp):
        print(temp.val,temp.next)
        temp=temp.next
        
        
if __name__=="__main__":
    compute()
        