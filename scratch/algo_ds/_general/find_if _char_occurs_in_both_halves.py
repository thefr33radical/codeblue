# find if same charecters occur in both the sides of array

def compute(string):
    n=len(string)
    dct={}
    
    if(n%2!=0):
        print("Same number of charecters dont occur")
        return
    else:
        for i in range(0,int(n/2)):
            if(string[i] not in dct.keys()):
                dct[string[i]]=1
            else:
                dct[string[i]]+=1
        for i in range(int(n/2+1),n):
            if(string[i] not in dct.keys()):
                print(" Unequal1",dct)
                return
            else:
                if(dct[string[i]]==-1):
                    print(" Unequal",dct)
                    return
                else:
                    dct[string[i]]-=1
                
        print(" Equal",dct)
        return
        

if __name__=="__main__":
    string="awbbbabe"
    compute(string)