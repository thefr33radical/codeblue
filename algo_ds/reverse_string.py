'''
https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

'''
#T(c)=O(n/2)

arr=[4, 5, 1, 2]

i=0
j=len(arr)-1

while i<j:
    #swap foremost & end positions of array
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1

print(arr)
    
