'''Given a string, calculate number of indexes such that the substring to left of the index 
and the substring to the right of the index contains characters that can form the string 
“programmer” .'''


def compute():
    string="pppppprogrammerbdmprogrammernprogrammerdnprogrammer"
    index=40
    i=index
    j=index
    
    d1=dict()
    d2=dict()
    
    while(i>0):
            if(string[i] not in d1):
                d1[string[i]]=1
                i-=1
            else:
                d1[string[i]]+=1
                i-=1
    
    while(j<len(string)):
            if(string[j] not in d2):
                d2[string[j]]=1
                j+=1
            else:
                d2[string[j]]+=1
                j+=1
        
                
    minimum=999
    for i in "programmer":
            if not i in d1:
                print("none possible in d1 break")
                break
            elif(d1[i]<minimum):
                minimum=d1[i]
                
            
    minimum2=999
    for i in "programmer":
            if not i in d2:
                print("none possible in d1 break")
                break
            elif(d2[i]<minimum2):
                minimum2=d2[i]
    
    print(minimum,minimum2) 
    
if __name__=="__main__":
    compute()