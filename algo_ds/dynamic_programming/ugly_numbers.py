
"""
Given n find the nth ugly numbers.
"""

import pickle
def isprime(number):
    for i in range(2,number):
        if number%i ==0:
            return False
    return True

def notprime(number):
    for j in range(6, number-1):
        if isprime(j):
            if number % j == 0:
               # print("false")
                return False
   # print("true")
    return True


if __name__=="__main__":
    # no= int(input())
    no = 11
    with open("storage_array.txt", "w") as f:
        storage = pickle.loads(f)

    if (len(storage) > no+1):
        print(storage[no][2])
    else:
        storage = []
        storage.append((1, 1))
        storage.append((2, 2))
        storage.append((3, 3))
        storage.append((4, 4))
        storage.append((5, 5))

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
        storage =[]
        storage.append((1,1))

        while i <= no :

            if ((number %2 == 0) or (number%3==0) or (number%5 ==0)) and notprime(number):
                print(i, number)
                storage.append((i, number))
                i+=1
                number+=1

            else:
                number+=1

        with open("storage_array.txt","w") as f:
            pickle.dumps(storage,f)

        #print(i-1,number-1)

