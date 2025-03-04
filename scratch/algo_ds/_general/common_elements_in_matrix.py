# Naive Implementation
count=0

matrix=[[1,2,3],[4,3,2,6,1],[8,2,1,7,8],[3,2,1,7]]
print(len(matrix))
for i in matrix[0]:
    count=0
    for j in range(1,len(matrix)):
        if(i in matrix[j]):
            count+=1
       # print(count)
        if(count==len(matrix)-1):
            print(i,"\nOccurs at all elements in the array")
