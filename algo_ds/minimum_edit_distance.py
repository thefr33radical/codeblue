"""
Minimum Edit Distance with equal weightage to delete,replace,insert
T(C)=O(3^m)
"""



def min_edit(str1,str2,len1,len2):
    if(len1==0):
        return len2
    if(len2==0):
        return len1

    if(str1[len1-1]==str2[len2-1]):
        return min_edit(str1,str2,len1-1,len2-1)

    else:
        return 1+ min( min_edit(str1,str2,len1-1,len2-1),
         min_edit(str1,str2,len1-1,len2),
          min_edit(str1,str2,len1,len2-1))
    

   

if __name__=="__main__":
    str1="sunday"
    str2="saturday"
    cost=min_edit(str1,str2,len(str1),len(str2))
    print(cost)