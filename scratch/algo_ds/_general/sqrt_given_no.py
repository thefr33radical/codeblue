'''
https://www.geeksforgeeks.org/flipkart-interview-set-8-sde-1/
Find the square root of a given integer. e.g 27 output should be 5, for 32 output should be 6.
'''
import math

def compute(x):
   # print((math.sqrt(x)),x**(1.0/2.0))
    y=(math.sqrt(x))
    if(y-int(y)>0.5):
        print(int(y)+1)
    else:
        print(int(y))


if __name__=="__main__":
    compute(25)

    