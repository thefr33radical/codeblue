'''
Given a number n, find the largest number small than having the same digits as of n. E.g. 231 output will be 213.
T(C)=O(n!)+ O(nlogn)+O(n)
'''


import itertools

def compute(string):
    print(sorted(list(itertools.permutations(string))))
    val=sorted(list(itertools.permutations(string)))

    l=[]    
    for i in range(len(val)):
        l.append("".join(list(val[i])))
        if("".join(list(l[i]))==string):
            print("".join(list(val[i-1])))
    

    


if __name__=="__main__":
    compute("534")