import random
class node(object):
    def __init__(self,value,ptr):
        self.val=value
        self.next=None
        
        
def find_mid(head):
    temp=head
    
    if(temp.next)
    
    while(temp.next.next):
        slo=temp.next
        fast=(temp.next).next
        temp=slo
    
    print(slo.val,fast.val)


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
        