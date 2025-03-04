# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# your code goes here
#python3
#implementation of lambda function

# A lambda fuction is an anonymous function 
#
#	defined by keyword lambda
#	
#	Can take any number or arguments but only one expression
#	
#	used whenever function objects are required
#	commonly used with filter(), map(), reduce()
	
	
#example 1
var=lambda x,y:(x+5)*(y+4)
print(var(12,3))

#example 2
# map()

far=lambda t : (float(9)/5) * t + 32
celsius=[23,33,56,12,45]
x=map(far,celsius)

#filter()
#similar to map, filter()function filters out which are true

y=filter(lambda x:x%2==0,celsius)

#for i in y:
#	print(i)


#reduce()
#reduce function () takes in two parameters reduce(func,list). It applies the function to f(l1,l2),f(l1,l2,l3),f(l1,l2,l3,l4)
#z=functiontools.reduce(f, [47,11,42,102,13])
#print (z)











