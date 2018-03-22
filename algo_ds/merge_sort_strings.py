
def sort(string,low,mid,high):
    start1=int(low)
    start2=int(mid)+1
    temp=[]
    mid=int(mid)
    high=int(high)
    
    while(start1<=mid and start2<=high):
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
              
    while(start1<=mid):
            temp.append(string[start1])
            start1+=1
    while(start2<=high):
            temp.append(string[start2])
            start2+=1

    '''
    Points to note:
    1.    Error in copying elements to exact dimension of the original array
    2.    Pass exact indexes for low,high(not the size)
    
    '''
    k=0
    for i in range(low,high+1):
        string[i]=temp[k]
        k+=1
    #print(string,temp,"low ",low," mid ",mid," high ",high)
    

def split(string,low,high):
    if(int(low)<int(high)):
        mid=(low+high)/2
        mid=int(mid)
       
        split(string,low,mid)
     
        split(string,mid+1,high)
        string=sort(string,low,mid,high)
        return string

def compute(string):
    (split(string,0,len(string)-1))

if __name__=="__main__":
    #string="124356387"
    string="qwertybduiop"
    l=list(string)
    #l=list(map(int,l))
    #print(l)
    #print(l)
    compute(l)
  #  print(string)
    print(l)


