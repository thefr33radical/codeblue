'''

Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Examples : 
Input 
0 2 5 7 
Output 
2 (0 XOR 2) 
Input 
0 4 7 9 
Output 
3 (4 XOR 7)

Constraints: 
2 <= N <= 100 000 
0 <= A[i] <= 1 000 000 000

'''

#T(C)=O(n^2)
def compute(l):
    m=99999999
    
    for i in range(len(l)):
	       
        for j in range(i+1,len(l)):
            if((l[i]^l[j])<m):
                m=i^j
                x=i
	           
                #print(min)
                 
            #print(l[i]^l[j],"----",l[i],l[j])
    return m

#T(C) = O(nlogn)
def compute2(l):
    m=99999999
    l=sorted(l)
    for i in range(len(l)-1):
	       
        if((l[i]^l[i+1])<m):
                m=(l[i]^l[i+1])
                #x=i
	           
                #print(min)
            
        print(l[i]^l[i+1],"----",l[i],l[i+1])
if __name__=="__main__":
    l=[2,4,6,2]
    compute2(l)