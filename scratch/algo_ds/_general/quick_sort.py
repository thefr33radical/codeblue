
import numpy
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def part(arr,low,high):
    pivot=arr[int(low)]
    i=int(low+1)
    j=int(high)
   # print (i,j,low,high)
    
    while(1):
        while(arr[i]<pivot and i<j):
            i=i+1
           # print(i)
        while(arr[j]>=pivot and j>=i):
            j=j-1
        if(i<j):
           arr[i],arr[j]= swap(arr[i],arr[j])
        else:
            break

    print(arr)
    arr[low]=arr[j]
    arr[j]=pivot
    
    return j


def sort(arr,low,high):
    if(low<high):
        pivot=part(arr,low,high)
       # print ("pivot",pivot)
        sort(arr,low,pivot-1)
        sort(arr,pivot+1,high)
    
    
if __name__=="__main__":
    arr=[23,45,67,76,34,2,12,68]
    sort(arr,0,len(arr)-1)
    print(arr)














