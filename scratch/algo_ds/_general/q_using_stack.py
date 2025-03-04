# implement queue using stack X2
'''
T(c)=O(n) X 2 for push and pop operations

'''

##############################################################################
#primary stack to store elements
class stack1(object):
    
    def __init__(self):
        self.item=list()
    def insert_front(self,val):
        self.item.append(val)
    def delete_front(self):
        z=int()
        if(self.item):
            z=self.item[0]
            del self.item[0]
            return z
#Secondary stack to copy elements when deleting and printing           
class stack2(object):
    
    def __init__(self):
        self.item=list()
    def insert_front(self,val):
        self.item.append(val)
        
        
    def delete_front(self):
        z=int()
        if(self.item):
            z=self.item[0]
            del self.item[0]
            return z
    
  
###########################################################################
#functons of a queue implemented on stack
  
  
def insert_front(obj,s1,s2):
    for i in range(6):
        s1.insert_front(obj[i])
    
def delete_rear(s1,s2):
    for i in range(len( s1.item)-1):
        z=s1.delete_front()
       # print("z",z)
        s2.insert_front(z)
     #   print ("s1",s1.item,"\n s2 ",s2.item)
        
    s1.delete_front()
    for i in range(len( s2.item)):
          z=s2.delete_front()
          s1.insert_front(z)
          
    print("after deletion : s1",s1.item,"s2 :",s2.item)
          
          
def print_elements(s1,s2):
    for i in range(len( s1.item)):
        z=s1.delete_front()
       # print("z",z)
        s2.insert_front(z)
     #   print ("s1",s1.item,"\n s2 ",s2.item)
        
    for i in range(len( s2.item)):
          z=s2.delete_front()
          s1.insert_front(z)
          print("Qeueue : ",z)
        
'''   print("\n The contents of queue implemented using 2 stacks are")
    for i in s2.item:
        print(i)
        
   '''     
###########################################################################

if __name__=="__main__":
    obj=[1,2,3,4,5,6,7] 

    s1=stack1()
    s2=stack2()
    
    #insert four elements
    insert_front(obj,s1,s2)
    #print queue
    print_elements(s1,s2)
    #delete element
    delete_rear(s1,s2)
    #print queue
    print_elements(s1,s2)
    #delete element
    delete_rear(s1,s2)
    #print queue
    print_elements(s1,s2)



    

'''

obj=[]
y=10
z=20
for i in range(5):
    a=stack1()
    
    for j in range(y,z):
        a.insert_front(j)
    y+=10
    z+=10
    obj.append(a)
for i in range(5):
    print(obj[i].item)
    
'''




