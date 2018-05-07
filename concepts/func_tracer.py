''''

function to trace the recursion stack : factorial of a number
'''
def func(n):
    print(n)
    if(n==0 or n==1):
        return 1
    if(n==2):
        return 2
    else:
       x=(n* func(n-1))
       print(x)
       return x
       
if __name__=="__main__":
    y=func(5)
    print(y)