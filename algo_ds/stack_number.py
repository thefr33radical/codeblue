'''
An expression consisting of some brackets was given. You have to print the bracket number when you are parsing the expression.
For eg. (a+(b*c))+(d/e)

Answer would be: 122133

'''


def compute():

    #string="((1+22)*3)-(4/2)"
    string="(a+(b*c))+(d/e)"
    
    stck=[]
    count=0
    numb=[]
    for i in string:
        if(not str.isdigit(i)):
            if(i=="("):
                count+=1
                numb.append(count)
                stck.append([i,count])
            if(i==")"):
                a=stck.pop()
                numb.append(a[1])
                
    
    print(numb)

if __name__=="__main__":
    compute()