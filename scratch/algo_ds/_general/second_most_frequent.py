'''
Second most frequent character
https://www.geeksforgeeks.org/c-program-find-second-frequent-character/


T(C)=O(n)X 3
'''

def compute(string):
    dct={}
    for i in string:
        if( i in dct):
            dct[i]+=1
        else:
            dct[i]=1
            
  #  del(max(dct.keys(), x=lambda x: dct[x]))
    z=(max(dct.keys(), key=(lambda x:dct[x])))
    del(dct[z])
    print(max(dct.keys(), key=(lambda x:dct[x])))
    
    

if __name__=="__main__":
    compute("aaaaabbbcc")