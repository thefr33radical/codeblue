from collections import Counter
# your code goes here
def list_count(n):
	# either pass x or write function def after x=int(input("enter elem"))
	count=0
	for i in n:
		#n is list of strings convert to int before comparison
		if(int(i) == x):
			count=count+1
	return(count)

# python3 has only input
#https://www.smallsurething.com/the-difference-between-input-and-raw_input-in-python/

s=input("enter spaced elem")
print("\n")
n=s.split()
x=int(input("enter elem"))
print("\n",list_count(n))

# complete alternative code in 1 line
print(Counter(n)[str(x)])
