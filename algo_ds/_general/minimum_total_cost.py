'''
Minimum total cost incurred to reach the last station
T(C)=O(n)

'''



def compute():
    arr= [10, 6, 11, 4, 7, 1]
    
    min_cost=arr[0]
    cur_cost=0
    p=5
    for i in range(0,len(arr)-1):
        temp=arr[i]-arr[i+1]
        cur_cost+=temp
        
        if(cur_cost<0):
            min_cost+=abs(cur_cost)
            #cur_cost=0
            break
        
    if(cur_cost>=0):
        min_cost=cur_cost
        
    print(min_cost*p)

if __name__=="__main__":
    compute()