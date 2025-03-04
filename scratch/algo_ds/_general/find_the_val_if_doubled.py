
def compute():
    arr= [ 2, 3, 4, 10, 8, 1 ]
    k = 2
    found=1
    while(found):
        if(k in arr):
            k+=k
            found=1
        else:
            found=0

    print(k)

if __name__=="__main__":
    compute()