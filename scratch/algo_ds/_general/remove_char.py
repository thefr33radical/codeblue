'''

Remove characters from the first string which are present in the second string
'''

#Solution 1 T(C)=O(n2)
def compute(string1,string2,string3):
    
    for i in string2:
        for j in string1:
            if(i==j):
                string1=string1.replace(i,"#")
                j="#"
                
    #print(string1)
    for i in string1:
        if(i!="#"):
            string3+=i
    print(string3)
    
#T(C)=O(n)+O(m)  +O(m)   
def compute2(string1,string2,string3):
    d={}
    for i in string1:
        d[i]=1
    
    for i in string2:
        if(i in d):
            string1=string1.replace(i,"#")
        
    for i in string1:
        if(i!="#"):
            print(i)
            
if __name__=="__main__":
    string1="geeksforgeeks"
    string2= "maskg"
    string3=""
    compute2(string1,string2,string3)