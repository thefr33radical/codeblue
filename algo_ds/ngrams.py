# -*- coding: utf-8 -*-
# Custom program to generate Ngrams

def next_words(text,i,n):
    s=""
    for i in range(i,n+1):
        s=s+text[i]
        print(s)
    return s
        
def generate_ngrams(text,n):
    n=n-1
    temp=[]
    for i in range(0,len(text)-n):
        temp.append(text[i]+next_words(text,i+1,i+n))
    return temp
    
string="i am not here sorry i will not be there" 
string=string.split()      
output=generate_ngrams(string,2)
print(output)
        

        
        
