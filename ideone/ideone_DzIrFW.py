# Enter your code here. Read input from STDIN. Print output to STDOUT


def func():
    
    x=raw_input()
    temp=x
    
    
    
    z=str(int(bin(5)[2:]))
    i=1
    t=1
    while i<=len(x):
    	t=t*5
    	z=str(int(bin(t)[2:]))
    	c=temp.count(z)
    	print c
    	i=i+1
    
    
   
func()