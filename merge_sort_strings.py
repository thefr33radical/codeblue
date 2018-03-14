
def sort(string,low,mid,high):
    start1=low
    start2=mid
    temp=[]
    
    while(start1<mid and start2<high):
        if(string[start1]<string[start2]):
            temp.append(string[start1])
            start11+=start1
        else:
            temp.append(string[start2])
            start2+=start2
            
        while(start1<mid):
            temp.append(string[start1])
            start11+=start1
        while(start2<high):
            temp.append(string[start2])
            start2+=start2
            
    string =temp
    return string
    
def split(string,low,high):
    if(low<high):
        mid=(low+high)/2
        split(string,low,mid)
        split(string,mid+1,high)
        sort(string,low,mid,high)
        return string
    
    
    

def compute(string):
    split(string,0,len(string))
    



if __name__=="__main__":
    string="abcdefgh"
    l=list(string)
    #print(l)
    a=compute(l)


