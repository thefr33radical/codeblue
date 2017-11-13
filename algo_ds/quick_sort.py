#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:26:34 2017

@author: gowtham
"""

import numpy
def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def part(arr,low,high):
    pivot=arr[low]
    i=int(low+1)
    j=int(high)
    print (i)
    while(1):
        while(arr[i]<pivot):
            i=i+1
        while(arr[j]>=pivot):
            j=j-1
        if(i<j):
           arr[i],arr[j]= swap(arr[i],arr[j])
        else:
            break

    print(arr)
    arr[low]=arr[i]
    arr[i]=pivot
    
    return i


def sort(arr,low,high):
    if(low<high):
        pivot=part(arr,low,high)
        print ("pivot",pivot)
        sort(arr,low,pivot-1)
        sort(arr,pivot+1,high)
    
    
if __name__=="__main__":
    arr=numpy.asarray([23,45,67,76,34,2,12,68],dtype=int)
    sort(arr,0,len(arr)-1)
    print(arr)














