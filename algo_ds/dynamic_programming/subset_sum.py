 """





ALgorithm to find if the sum N is possible from the subset { } 0f m numbers using DP

1. Construct a matrix  MAT of m+1 X N+1 matrix. matrix[i][0]=1;

2. Initialize  column to MAT[i][0]= 1, MAT[0][i] =0, because a 0 can be formed by empty subset.

3. for i=1 to m+1
	for j=1 t0 n+1
		if MAT[i]<MAT[j]
			MAT[i][j]=MAT[i-1][j-i]

		else
			MAT[i][j]=MAT[i-1][j-1]

4. Return MAT[m][N]


"""



def subset_sum():
	array = [1,3,4,7]
	total = 6
	matrix = [ [0]*(total+1) for i in range(0,len(array)+1) ]

	for i in range(0,len(matrix)):
		matrix[i][0]=1
		
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[i])):
			if j<array[i-1]:
				matrix[i][j]=matrix[i-1][j]
			else:
				matrix[i][j]=matrix[i-1][j] or matrix[i-1][j - array[i-1]]
				
				
	print(matrix)
	print(matrix[len(matrix)-1][len(matrix[0])-1])

