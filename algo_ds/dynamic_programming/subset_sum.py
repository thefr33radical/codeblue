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
