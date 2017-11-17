#
from sys import stdin,stdout
import array
def insertion_sort(arr):
  # j=(int(1))
    key=0    
    for i in range(len(arr)):
        key=arr[i]
        #print(i)
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j=j-1
  #  print (i)
    #i=i+1
        arr[j+1]=key
    return (arr)
        
        
        
        
    
    


if __name__=='__main__':

    arr=[69,1,2,223,45,34,788,897,21,45]
    #print(len(arr))
    arr=array.array('i',arr)
    arr=insertion_sort(arr)
    for i in arr:
        print (i,"\t")