import random
class node(object):
    def __init__(self,value,ptr):
        self.val=value
        self.next=None
        
        
def find_mid(head,tail):
    sloptr=head
    fastptr=head
    
    if(sloptr and fastptr is None):
        return None
        
    if(fastptr is None):
        return sloptr
    
    while(sloptr.next):
        sloptr=sloptr.next
        if(fastptr.next):
            if((fastptr.next).next):
                fastptr=(fastptr.next).next
        else:
            return sloptr
                
                


def ms(head,low,high):
    mid=find_mid(low,high)

def compute():
    head=node(4,None)
    g=[]
    prev=head
    for i in range(10):
        
        g=node(random.randint(1,500),None)
        prev.next=g
        prev=g
        
      
    
   
    temp=head
    while(temp):
        print(temp.val,temp.next)
        temp=temp.next
        
        
if __name__=="__main__":
    compute()
        