'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def flood_fill(arr,i,j,prev,new):
    if(i<0 or i>=len(arr) or j< 0 or j>=len(arr[0])):
        return 0
    if(arr[i][j]!=prev):
        return 0
    
    if(i==len(arr)-1 and j==len(arr[0])-1):
        #val="Yes"
        return 1
        
    arr[i][j]=new
    if(flood_fill(arr,i-1,j,prev,new) or    flood_fill(arr,i+1,j,prev,new) or 
    flood_fill(arr,i,j-1,prev,new) or
    flood_fill(arr,i,j+1,prev,new)):
        #print("Yes")
        return 1
    else:
        return 0
    
    
    
    

# Write your code here
inp=input()
#print(inp)

l=inp.split()
#print(l)
val="No"
arr=[]
temp=[]
for i in range(int(l[0])):
    
    inp=input()
    temp=list()
    #temp=temp.clear()
    temp=inp.split()
    arr.append(temp)
    #temp=temp.clear()
    
for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j]=="1"):
                arr[i][j]="X"
                
#print(arr)
if(flood_fill(arr,0,0,"X","1")):
    print("Yes")
else:
    print("No")
#print(val)
