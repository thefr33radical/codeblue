'''

https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/


'''

#method 1 dictionary (O(n) X 3)
def compute(string1,string2):
    dct={}
    for i in string1:
        if(i in dct):
            dct[i]=dct[i]+1
        else:
            dct[i]=1
            
    for i in string2:
        if(i in dct):
            dct[i]=dct[i]-1
        else:
            print("Not an anagram")
            return
            
        
    for i in dct.keys():
        if(dct[i]!=0):
            print("Not Anagaram",dct[i])
            return
       
    print("Anagram")

# Method  2 : Sort strings and compare ( O(nlogn)+O(n))
def compute2(string1,string2):
    s1="".join(sorted(string1))
    s2="".join(sorted(string2))
    i=0
    if(len(s1)!=len(s2)):
        print("Not Anagram ")
        return
        
    while(i<len(s1)):
        if(s1[i]!=s2[i]):
            print("Not Anagram ")
            return
        i=i+1   
    print("Anagram",s1,s2)

if __name__=='__main__':
    string1="listel4n"
    string2="silentl"
    compute2(string1,string2)