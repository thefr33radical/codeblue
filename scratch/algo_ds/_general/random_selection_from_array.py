# selecting  a random number and check if its equal to the given number
# T(O) : O(n)

import random
def compute():
    pass
    arr=[1,2,4,3,43,56,7,8,12,87,92,60]
    key=23  
   # print(random.choice(arr))
    n=len(arr)-1
    for i in range(n):
        t=random.randint(0,n)
        if(key==arr[t]):
            print("found element",arr[i],i)
        else:
            if(n>0):
                tmp=arr[n]
                arr[n]=arr[t]
                arr[t]=tmp
               
                print("swapped elements : ",arr[t],arr[n],"------ index :",t,":",n)
                n=n-1
                print(arr)
            
    
if __name__=='__main__':
    compute()