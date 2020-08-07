'''
https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

T(C) = O(m x n)

'''


def compute(mat):
    left=0
    right=len(mat[0])-1
    up=0
    down=len(mat)-1
    
    left1=0
    right1=len(mat[0])-1
    up1=0
    down1=len(mat)-1
    origleft=0
    origright=len(mat[0])-1
    origup=0
    origdown=len(mat)-1
    
    
    while((left<right or up<down)):
        print("\n righttop ")
        while(left <right):
            print(mat[up][left])
            left+=1
        print("\n rightdown")
        while(up<down):
            print(mat[up][left])
            up+=1
        print("\n downleft")
        while(right1>left1):
            print(mat[up][right1])
            right1-=1
        print("\n topleft")
        while(down1>up1):
            print(mat[down1][right1])
            down1-=1
        print("\n")
        origleft+=1
        origright-=1
        origup+=1
        origdown-=1
        
        left=origleft
        right=origright
        up=origup
        down=origdown
        right1=origright
        left1=origleft
        up1=origup
        down1=origdown
 

if __name__=="__main__":
    mat=[[i for i  in range(1,5)]]*5
    print(mat)
    compute(mat)
    