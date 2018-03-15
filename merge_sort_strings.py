string="123657842234"
def sort(string,low,mid,high):
    start1=int(low)
    start2=int(mid)
    temp=[]
    mid=int(mid)
    high=int(high)
    
    while(start1<mid and start2<high):
        if(string[start1]<(string[start2])):
            temp.append(string[start1])
          #  print(string[start1],"<",(string[start2]))
          #  print(temp)
            start1+=1
        else:
            temp.append(string[start2])
          #  print(string[start2],"<",(string[start1]))
          #  print(temp)
            start2+=1
              
    while(start1<mid):
            temp.append(string[start1])
            start1+=1
    while(start2<high):
            temp.append(string[start2])
            start2+=1

    
    if(len(temp)>0):
       string =temp
    return string

def split(string,low,high):
    if(int(low)<int(high)):
        mid=(low+high)/2
        mid=int(mid)
       
        split(string,low,mid)
     
        split(string,mid+1,high)
        string=sort(string,low,mid,high)
        return string

def compute(string):
    print(split(string,0,len(string)))

if __name__=="__main__":
    #string="124356387"
    l=list(string)
    l=list(map(int,l))
    #print(l)
    #print(l)
    compute(l)
   # print(string)


