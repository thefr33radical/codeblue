import numpy as np
def insertion_sort(arr):
    i=int(0)
    j=(int(1))
    key=0    
    while (i<len(arr)):
        key=arr[i]
        print(i)
        while(j>=0 and arr[j]<key):
            arr[j-1]=arr[j]
            j=j-1
    print (i)
    i=i+1
    arr[j]=key
    return (arr)
        
        
        
        
    
    


if __name__=='__main__':

    arr=[1,2,223,45,34,788,897,21,45]
    #print(len(arr))
    arr=np.array(arr,dtype=int)
    arr=insertion_sort(arr)
    print (arr)