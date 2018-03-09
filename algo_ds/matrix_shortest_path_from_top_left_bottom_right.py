'''Given a matrix, write a code to calculate the shortest path from left-top most element,
 to the right-bottom most element, 
 such that at each step the value is multiplied with the previous value,
 the final value should have least number of zeros.  
 '''
 
 
cost=[[1,1,2],[15,1,16],[25,3,5]]

mat=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def min_func(i,j):
    if(i<=j):
        return i
    else:
        return j

def min_search(mat,i,j):
    if(i==2 and j ==2):
        return 15
    elif (i==2):
        return  (i,j+1)
        pass
    elif(j==2):
        return  (i+1,j)
    else:
        if(mat[i][j]*mat[i][j+1]<=(mat[i][j]*mat[i+1][j] and mat[i][j]*mat[i+1][j+1])):
            return (i,j+1)
            
        if(mat[i][j]*mat[i+1][j]<= (mat[i][j]*mat[i+1][j+1]and mat[i][j]*mat[i][j+1])):
            return (i+1,j)
            
        else:
            return (i+1,j+1)
        

mat[0][0]=cost[0][0]
for i in range(1,3):
          mat[i][0]=mat[i-1][0]*cost[i][0]
for j in range(1,3):
    mat[0][j]=mat[0][j-1]*cost[0][j]
   
print(mat)
for i in range(1,3):
    for j in range(1,3):
         mat[i][j]=min(mat[i-1][j],mat[i-1][j-1],(mat[i][j-1]))*cost[i][j]
print(mat)
        
        