# min cost path : side and down movements allowed
# T(c)=O(n^2)





mat=[[1,3,5,8],[4,2,1,7],[4,3,2,3]]
val=[ [0,0,0,0],[0,0,0,0],[0,0,0,0]]

val[0][0]=mat[0][0]
for i in range(1,len(mat[0])):
    val[0][i]=mat[0][i]+val[0][i-1]
 #   print(val)
    

for j in range(1,len(mat)):
    val[j][0]=val[j-1][0]+mat[j][0]

#print(len(mat),len(mat[0]))    
    
for i in range(1,len(mat)):
    for j in range (1,len(mat[0])):
        val[i][j]=min(val[i-1][j],val[i][j-1])+mat[i][j]
       # print(i,j)
        #)
        
print(val)
path=[[len(mat)-1,len(mat[0])-1]]

#Tracing the path <<<  path depends on uneven decrement so use while loops
i=len(mat)-1
j=len(mat[0])-1
while(i>0):
   while(j>0):
        if(val[i-1][j]<=val[i][j-1]):
            path.append([i-1,j])
            i=i-1
            # print(i,j)
        else:
            path.append([i,j-1])
            j=j-1
            
            ##print(i,j)
            
print(path)

for i in path:
    print(mat[i[0]][i[1]])

'''            
print(mat)
print(val)


'''