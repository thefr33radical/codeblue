'''
Given an unsorted array – arr find a pair arr[i] & arr[j] such that  arr[i]<arr[j] & i<j and (arr[i] + arr[j]) is maximum. 
Expected time complexity – O(n)

'''


def compute():
    
    arr=[9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    arr=[1, 2, 3, 4, 5, 6]
    arr=[6, 5, 4, 3, 2, 1]
    arr=[34, 8, 10, 3, 2, 80, 30, 33, 1]
    maximum=-1
    for i in range(0,len(arr)-2):
        for j in range(1,len(arr)-1):
            for k in range(2,len(arr)):
                if(i<j<k):
                    if(arr[i]<arr[j]<arr[k]):
                        if(arr[i]+arr[j]+arr[k]>maximum):
                            maximum=arr[i]+arr[j]+arr[k]
                        
    print(maximum)
if __name__=="__main__":
    compute()