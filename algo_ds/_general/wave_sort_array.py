
'''
https://www.geeksforgeeks.org/sort-array-wave-form-2/

 Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
 Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} OR
                 {20, 5, 10, 2, 80, 6, 100, 3} OR
                 
                 '''
                 
# method 1 : Sort array and swap elements
#T(C)=O(nLogn)
                 
                 
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b
    
def compute(arr):
    arr=sorted(arr) 
    i=1
    while i < len(arr)-1:
        arr[i],arr[i+1]=swap(arr[i],arr[i+1])  
        i+=2
        
    print(arr)
 
# method 2: make sure even elements are greated than neighbouring odd elements
#T(C)=O(n)
 
def compute2(arr):
    i=2
    
    if(arr[0]<arr[1]):
        arr[0],arr[1]=swap(arr[0],arr[1])
    while i <len(arr)-1:
        if(arr[i]<arr[i-1]):
            arr[i],arr[i-1]=swap(arr[i],arr[i-1])
            
        if(arr[i]<arr[i+1]):
            arr[i],arr[i+1]=swap(arr[i],arr[i+1])
            
        i+=2
        
    print(arr)
                
if __name__=="__main__":
    arr= [10, 5, 6, 3, 2, 20, 100, 80]
    compute(arr)
    compute2(arr)