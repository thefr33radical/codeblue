'''


'''

def compute():
    mat=[[ 1   ,  2  ,   3 ,    4], 
    [5  ,  6  ,  7  ,  8],
    [9  ,  10   , 11   , 12],
     [13  ,  14   ,15   , 16],
   [17   , 18  , 19    ,20]]
    
   
    for i in range(0,len(mat[0])):
        j=0
        k=i
        while j<=i:
            while k>=0 :                
                print(mat[k][j])
                k-=1
                j+=1
        print("\n")
            
    for i in range(len(mat[0])-1,-1,-1):
        j=0
        k=i
        while j<=i:
            while k>=0 :                
                print(mat[j][k])
                k-=1
                j+=1
        print("\n")
            
            
            
           


if __name__=="__main__":
    compute()