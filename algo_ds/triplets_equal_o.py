''' Triplets whose sum equals to 0 '''





def compute():
    arr=[0, -1, 2, -3, 1]    
    for i in range(0,len(arr)-2):
        if(arr[i]!=arr[i+1] and arr[i]!=arr[i+2] and arr[i+2]!=arr[i+1]):
            if(arr[i]+arr[i+1]+arr[i+2]==0):
                print("triplet found")
                print(arr[i],arr[i+1],arr[i+2])


if __name__=="__main__":
    compute()