'''
https://www.geeksforgeeks.org/number-subarrays-sum-less-k/
(Implementation wrong)
T(C)=O(n3)

'''

def compute():
    arr = [1, 11, 2, 3, 15]
    k= 25
    
    window=1
    
    while(window<len(arr)):
        i=0
        
        
        while(i<(len(arr)-window)):
            sumer=0
            temp=[]
            for j in range(i,i+window+1):
                #print(arr[j])
                temp.append(arr[j])
                sumer+=arr[j]
                if(sumer>k):
                    print(sumer)
                    print(temp)
                    print("\n")
            i+=1
            
            
        window+=1
       # break   
        #window+=1

if __name__=="__main__":
    compute()