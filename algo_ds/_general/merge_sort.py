#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:13:25 2017

@author: gowtham
"""
def sorter(arr,low,mid,high):
    start1=low
    start2=mid+1
    temp=[]
    
    start1=int(start1)
    start2=int(start2)
    while(start1<=mid and start2<=high):
        if(arr[start1]<arr[start2]):
            temp.append(arr[start1])
            start1=start1+1
        else:
            temp.append(arr[start2])
            start2=start2+1
            
    while(start1<=mid):
        temp.append(arr[start1])
        start1=start1+1
        
    while(start2<=high):
        temp.append(arr[start2])
        start2=start2+1
        
    arr=temp        
        
    

def merge(l,low,high):
    if(int(low)<int(high)):
        mid=(low+high)/2
        merge(l,low,mid)
        merge(l,mid+1,high)
        sorter(l,low,mid,high)

if __name__=='main':
    l=[34,343,54,5,555,85]
    
else:
    l=[34,343,54,5,555,85]
    l.sort()
    merge(l,0,int(len(l)-1))
    print (l)