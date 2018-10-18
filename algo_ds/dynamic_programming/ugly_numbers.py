
"""
Given n find the nth ugly numbers.
"""

def notprime(number):
    for j in range(6, number-1):
        if number % j == 0:
            print("false")
            return False
    print("true")
    return True


if __name__=="__main__":
   # no= int(input())
    no =11

    if no == 1:
        print("1")
    if no ==2 :
        print("2")
    if no ==3:
        print("3")
    if no ==4:
        print("4")
    if no ==5:
        print("5")

    number =6
    i=6
    while i <= no :

        if (number %2 == 0) or (number%3==0) or (number%5 ==0) and notprime(number):
            print(i, number)
            i+=1
            number+=1

        else:
            number+=1

    #print(i-1,number-1)

