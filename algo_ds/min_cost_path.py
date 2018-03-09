#min cost path
# T(c)=O(n^2)





mat=[[1,3,5,8],[4,2,1,7],[4,3,2,3]]
val=[ [0,0,0,0],[0,0,0,0],[0,0,0,0]]

val[0][0]=mat[0][0]
for i in range(1,len(mat[0])):
    val[0][i]=mat[0][i]+val[0][i-1]
    print(val)
    
mat2=[[0]*5]*5
print(mat2)