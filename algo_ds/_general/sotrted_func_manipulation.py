
def func(a):
    return a[0]


def compute():
    l=[[9,2],[1,2],[5,2],[6,2]]
    
    x=sorted(l,key=func)
    print(x)


if __name__=="__main__":
    compute()