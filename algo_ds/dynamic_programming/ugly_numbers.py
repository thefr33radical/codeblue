
"""
Given n find the nth ugly numbers.
"""


if __name__=="__main__":
   # no= int(input())
    no =8

    if no == 1:
        print("1")
    if no ==2 :
        print("2")
    if no ==3:
        print("3")
    if no ==4:
        print("5")

    number =6
    i=5
    while i <= no:
        if number %2 == 0 and number%3==0 and number%5 ==0:
            is_ugly=1
            for j in range(6,number):
                if number%j ==0:
                    is_ugly =0
                    break
            if is_ugly ==1:
                i+=1
                number+=1
            else:
                number+=1

        else:
            number+=1

    print(number)

