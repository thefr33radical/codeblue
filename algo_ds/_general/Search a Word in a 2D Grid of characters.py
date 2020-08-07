#Search a Word in a 2D Grid of characters

'''

Input:  grid[][] = {"GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"};
        word = "GEEKS"

Output: pattern found at 0, 0
        pattern found at 0, 8
        pattern found at 1, 0
        
        '''
        

def compute(string,keys):
    i=0
    count=0
    pos=0
    while pos <(len(keys)):
        while i < (len(string)):
            j=0
            while j < (len(string[i])):
                if(string[i][j]==keys[pos]):
                    i=i+1
                    pos=pos+1
                    if(pos==len(keys)):
                        print("found element")
                        break
                    
                    
            




if __name__=="__main__":
    grid= ["GEEKSFORGEEKS",
                    "GEEKSQUIZGEEK",
                    "IDEQAPRACTICE"]
                    
    string=[]
    for i in grid:
        a=[]
        for j in i:
            a.append(j)
        string.append(a)
        
    print(string)
    compute(string,"geeks")
        
        