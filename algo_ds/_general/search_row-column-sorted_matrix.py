'''
https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

T(C)=O(n)

'''
mat = [ [10, 20, 30, 40],
                      [15, 25, 35, 45],
                      [27, 29, 37, 48],
                      [32, 33, 39, 50]]
                      

j=len(mat[0])-1
i=0
key=38
while(i<len(mat) and j>=0):
    if(mat[i][j]==key):
        print("\n key found at pos ",i,j)
        break
        
    if(mat[i][j]>key):
        j=j-1
    else:
        i=i+1
    

