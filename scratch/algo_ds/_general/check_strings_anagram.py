from sys import stdin,stdout
#str1=stdin.readline()
#str2=stdin.readline()

str1="i am here"
str2="i am not here"
d1={}
d2={}
for i in str1:
    d1[i]=1

for i in str2:
    if (i is not in d2):
        d2[i]=1
    else:
        d2[i].item+=1
    
if (d1==d2):
    stdout.write("both are equal")
    
print(d1,d2)
    
