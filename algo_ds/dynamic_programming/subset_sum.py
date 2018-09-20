 """





ALgorithm to find if the sum N is possible from the subset { } 0f m numbers using DP

1. Construct a matrix  MAT of m+1 X N+1 matrix. 
2. Initialize  column to MAT[#][0]= { subset }, MAT[#][1] =1, because a 0 can be formed by empty subset. Mat[0][#] to 1~N.
3. for i=1 to m+1
	for j=1 t0 n+1
		if MAT[i]<MAT[j]
			MAT[i][j]=MAT[i-1][j-i]

		else
			MAT[i][j]=MAT[i-1][j-1]

4. Return MAT[m][N]


"""






N=8
a= [3,4,5,1,2]

mat =[ [0]*(N+1) for i in range(len(a)+1)]

#mat= [row for i in range(0,(N))]

for i in range(1,len(a)+1):
    mat[i][0]=a[i-1]

for i in range(1,N+1):
    mat[0][i]=mat[0][i-1]+1


for i in range(1,N+1):
    for j in range(1,len(a)):

        if a[i-1]<mat[0][i-1]:
            mat[i][j]=mat[i-1][j-i]



print(mat)



