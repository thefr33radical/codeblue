'''Given a binary string, 
 find maximum substring length with equal number of 0’s and 1’s.
'''

def count_0(arr):
    count=0
    for i in arr:
        if(i=="0"):
            count+=1
    return count

def count_1(arr):
    count=0
    for i in arr:
        if(i=="1"):
            count+=1
   # print(count)
    return count  


def print_arr(arr,start,end,maximum):
    temp=[]
    for i in range(start,end):
        temp.append(arr[i])
  #  print(temp)
    ones=count_1(temp)
    zeroes=count_0(temp)
    if(ones==zeroes and ones>maximum):
        maximum=ones
    return maximum
    
def compute():
        arr="101100110"
        d1=[]
        d2=[]
        window=len(arr)
        maximum=0
        i=0
        #print(maximum)
        while(window>0):
            i=0
            
            while(i<len(arr)):
                start=i
                end=window+i
                if(end<len(arr)):
                    maximum=print_arr(arr,start,end,maximum)
                
                i+=1
            window-=1
            
        print(maximum)
        
        
if __name__=="__main__":
    compute()