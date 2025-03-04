'''
https://www.geeksforgeeks.org/find-sum-of-all-elements-in-a-matrix-except-the-elements-in-given-row-andor-column-2/


Example:
mat[][]  = [ [1, 1, 2]
             [3, 4, 6]
             [5, 3, 2] ]
Array of Cell Indexes: [(0, 0), (1, 1), (0, 1)]
Output:  15, 10, 16

T(C)=O(m X n)
#break vs continue
break- will completely exit the loop
continue- will stop the current statement but will follow through the next iteration of the loop

'''

mat= [ [1, 1, 2],
             [3, 4, 6],
             [5, 3, 2] ]
        
x=0
y=0
total=0
for i in range(len(mat)):
    if(x==i):
        continue
    for j in range(len(mat[0])):
        if(y==j):
            continue
        else:
            total+=mat[i][j]
            
print(total)
        
'''
method 2:
precomute sum of entire matrix, individual rows, individual columns

ans=sum-row[i]-col[j]+arr[i][j]
'''

