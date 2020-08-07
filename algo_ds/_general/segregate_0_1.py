'''
https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
'''

#T(C)=O(n)






def compute():
    arr= [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
    i=0
    j=len(arr)-1
    while i<len(arr) and j >=0:
        if(arr[i]==1):
            if(arr[j]==0):
                print(arr[i],arr[j])
                arr[i],arr[j]=arr[i],arr[j]
                i+=1
                j-=1
            else:
                while(arr[j]!=0 and j >=0):
                    j-=1
        elif(arr[i]==0):
            i+=1
    print(arr)
    


if __name__=="__main__":
    compute()
