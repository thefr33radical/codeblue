
matrix=[[1,2,-1,4],[-8,-3,4,2],[3,8,10,-8],[-4,-1,1,7]]
k=3
sumer=0
present_sum=0
x=0
y=0
for i in range(0,3):
    for j in range(0,3):
        present_sum=0
        if(i+k<4 and j+k <4):
            for p in range(i,i+k):
                for q in range(j,j+k):
                    present_sum+=matrix[p][q]
        
        if(present_sum>sumer):
            sumer=present_sum
            x=p
            y=q
            print(sumer,x,y)