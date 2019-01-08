

def msort(arr1,arr2):
	start1=0
	start2=0
	end1=len(arr1)-1
	end2=len(arr2)-1
	c=[]
	
	while(start1 <= end1 and start2 <= end2):
		if(arr1[start1] < arr2[start2]):
			c.append(arr1[start1])
			start1+=1
		elif(arr2[start2] <= arr1[start1]):
			c.append(arr2[start2])
			start2+=start2
			
	while(start1 <= end1):
		c.append(arr1[start1])
		start1+=1
	while(start2 <= end2):
		c.append(arr2[start2])
		start2+=1
		
	return c
		
		
		
arr=[ [1,2,3],[4,5,6],[17,18,23],[15,16,19]]

c= msort(arr[0],arr[1])
print(c,len(arr))

for i in range(2,len(arr)-1):

	c= msort(c,arr[i])
	print(arr[i],i)
	
print(c)


