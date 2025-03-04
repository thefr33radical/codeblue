'''

Q2. Given a matrix with ‘X’ and ‘O’, change each ‘O’ to ‘#’ which are surrounded by ‘X’.

'''
def flood_fill(inp,i,j,prev,new):
    if(i<0 or i>= len(inp) or j <0 or j>=len(inp[i])):
        return
    if(inp[i][j]!=prev):
        return
    inp[i][j]=new
    print(inp[i][j])
    flood_fill(inp,i+1,j,prev,new)
    flood_fill(inp,i,j+1,prev,new)
    flood_fill(inp,i-1,j,prev,new)
    flood_fill(inp,i,j-1,prev,new)
    
def compute():
    inp =            [['X', 'O', 'X', 'X', 'X', 'X'],
                     ['X', 'O', 'X', 'X', 'O', 'X'],
                     ['X', 'X', 'X', 'O', 'O', 'X'],
                     ['O', 'X', 'X', 'X', 'X', 'X'],
                     ['X', 'X', 'X', 'O', 'X', 'O'],
                     ['O', 'O', 'X', 'O', 'O', 'O']
                     ]
                    
    for i in inp:
        for j in range(len(i)):
            if(i[j]=="O"):
                i[j]="-"
    
    #top    
    for i in range(len(inp[0])):
        if(inp[0][i]=="-"):
           # print("-")
            flood_fill(inp,0,i,"-","O")
    #right       
    for i in range(len(inp)):
        if(inp[i][len(inp[0])-1]=="-"):
            #print("-")
            flood_fill(inp,i,len(inp[0])-1,"-","O")
    #bottom
    for i in range(len(inp[len(inp)-1])):
        if(inp[len(inp)-1][i]=="-"):
           # print("-")
            flood_fill(inp,len(inp)-1,i,"-","O")
    #left
    for i in range(len(inp)):
        if(inp[i][0]=="-"):
            print("-")
            flood_fill(inp,i,0,"-","O")
    
    for i in inp:
        for j in range(len(i)):
            if(i[j]=="-"):
                i[j]="X"
   
    for i in inp:
        print(i)
    
if __name__=="__main__":
    compute()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    