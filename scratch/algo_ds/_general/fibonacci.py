# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:09:27 2017

@author: gowtham
"""
import os


def compute(num):
    if(num == 1 or num == 2):
        return (1)
        
    else:
        z=num-1
        r=num-2
        p=(compute(z)+compute(r))
        yield p
        
for i in compute(6):
    print(i)