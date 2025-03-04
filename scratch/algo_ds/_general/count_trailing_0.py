
#wrong
def count(num):
    count=0
    print(num&1)
    while((num&1)==1):
        num=num>>1
        print(num,"\n")
        count+=1
        
    print("Count : ",count)
        
if __name__=="__main__":
    count(11)     