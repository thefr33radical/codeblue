
def print_arr(arr,start,end):
    for i in range(start,end):
        print(arr[i])
    print("\n")

def compute():
    arr="101100110"
    d1=[]
    d2=[]
    window=1
    i=0
    
    
    while(window<4):
        i=0
        
        while(i<len(arr)):
            start=i
            end=window+i
            if(end<len(arr)+1):
                print_arr(arr,start,end)
            i+=1
        window+=1
        
        
        


if __name__=="__main__":
    compute()