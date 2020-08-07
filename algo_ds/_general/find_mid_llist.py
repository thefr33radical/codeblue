import random
class node(object):
    def __init__(self,value,ptr):
        self.val=value
        self.next=None
        
        




def compute():
    head=node(4,None)
    a=[1,2,3,4,5,6,7,8,9,10,11]
    prev=head
    j=0
    for i in range(10):
        
        g=node(a[j],None)
        j+=1
        prev.next=g
        prev=g
        
      
    
   
    temp=head
    fastptr=temp
    sloptr=temp
    count=0
    while(sloptr.next):
            sloptr=sloptr.next
            if((fastptr.next)):
                if((fastptr.next).next):
                    count+=1
                    fastptr=(fastptr.next).next
                else:
                    #print(count,sloptr.val)
                    break
                    
            else:
                print(count,sloptr.val)
                break
                
                
            
        
        
if __name__=="__main__":
    compute()
        