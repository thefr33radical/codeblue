

class node(object):
    def __init__(self):
        self.kids=[0]*26
        self.isleaf=False
        self.val=[None]*26        

class t(object):
    def __init__(self):
        self.l=[]
        
    def insert_(self,head,string):
        temp=head
        for i in string:
            index=ord(i)-ord('a')
            if(temp.kids[index]==0):
                temp.kids[index]=1
                temp.val[index]=node()
                temp=temp.val[index]
            else:
                 temp=temp.val[index]
        temp.isleaf=True
        return
                 
    def print_(self,head,string):
        temp=head
       # print(string,self.l,temp.ssisleaf)
        for i in range(len(temp.kids)):
            if(temp.kids[i]==1):
                self.print_(temp.val[i],string+chr(ord('a')+i))
            if(temp.isleaf==True):
                self.l.append(string)
                
                break
        
        return
        
if __name__=="__main__":
    n=node()
    a=t()
    for i in (["gowthm","mahesh","sujau","mohan","mandeep"]):
        a.insert_(n,i)
    a.print_(n,"")
    print(a.l)
                