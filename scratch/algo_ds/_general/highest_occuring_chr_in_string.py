# Highest occuring char in string

#O(n) = O(n) +O(n)
#O(n) = Construct a hash map + find max in a hash map

def compute_naive(string):
    dct={}
    
    for i in string:
        if(i in dct.keys()):
            dct[i]=1+dct[i]
        else:
            dct[i]=1

    #get the maximum value in  a dciionary using lamba function
    print(max(dct.keys(), key=(lambda k: dct[k])))
    print(dct)


if __name__=="__main__":
    string="abddssfkwenfnonnfowenofnwejhdbjcbxnkxwlnnrf"
    compute_naive(string)