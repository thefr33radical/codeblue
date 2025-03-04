
# Perform all perutaions of a given string

def swap(l,a,b):
    temp=l[a]
    l[a]=l[b]
    l[b]=temp
    
def permute(l,k,n):
    if(k==n-1):
        print(l)
        return
    else:
       # print(l)
        for i in range(k,n):
            swap(l,k,i) # fixed letter swap
            permute(l,k+1,n)
            swap(l,k,i)
                
def compute(string):
    l=sorted(string)    
    
    permute(l,0,len(l))
    

if __name__=="__main__":
    compute("abcd")