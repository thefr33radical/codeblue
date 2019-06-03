# Recursive digit sum

#!/bin/python3

import math
import os
import random
import re
import sys


def no_of_dig(num):
    count =1
    while int(num/10) > 0:
        num=num%10
        count+=1

    return count

def rec_find(num):
    if no_of_dig(num)==1:
        return num
    else:
        sdg= 0
        #print("number",num)
        while int(num) > 0:
            rem=num%10
            sdg+=rem
            num =int(num/10)
        #print("superdigit",sdg)
        return rec_find(sdg)
        
        

# Complete the superDigit function below.
def superDigit(n, k):
    sub =n
    for i in range(k-1):
        n+=sub
    n=int(n)
    return rec_find(n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
