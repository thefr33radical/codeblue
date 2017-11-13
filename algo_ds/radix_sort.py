import numpy as np
def count_sort(arr,exp):
    counter=np.zeros(10,dtype=int)
    output=np.zeros(len(arr),dtype=int)
              
    for i in range(0,len(arr)):
        z=int((arr[i]/exp)%10)
        #print (z)
        counter[z]=counter[z]+1
       # print (i)
       # print(counter)
        
    #print (counter)
    for i in range(1,len(counter)):
        counter[i]=counter[i-1]+counter[i]
        
    #print(counter)
    i=len(arr)-1
    while(i>=0):
         output[ int(counter[int((arr[i]/exp)%10)])-1]=arr[i]
         counter[int((arr[i]/exp)%10)]= counter[int((arr[i]/exp)%10)]-1
         i=i-1
    print (counter,output)
    #rint (arr)     
    #arr=output
    for i in range(0,len(arr)):
        arr[i]=output[i]
    return arr

def sorter(arr):
    max_ele=max(arr)
    print(max_ele)
    i=1
    while (int(max_ele/i))>0:
        arr=count_sort(arr,i)
        i=i*10
        #print(i)
    return arr

if __name__=='__main__':

    arr=[1,2,223,45,34,788,897,21,45]
    #print(len(arr))
    arr=np.array(arr,dtype=int)
    arr=sorter(arr)
    print (arr)