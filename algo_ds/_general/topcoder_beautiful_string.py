'''
Definition: a string is beautiful if it has two consecutive equal characters. Examples of beautiful strings are "KEEP", "ZZZZZ" and "TTORR", while the following are not beautiful: "A", "GH" and "ABCABCBX".
You are given the String S and you are going to remove exactly one character from S. Is it possible that the new string will be beautiful? If yes, return "Possible". Otherwise, return "Impossible".

Note that the return value is case-sensitive.


Examples
0)	
    	
"VIKING"
Returns: "Possible"
You can remove 'K' to obtain the string "VIING". This string is beautiful because it has two consecutive 'I'.
1)	
    	
"BCAB"
Returns: "Impossible"
You can only get one of the following strings: "CAB", "BAB", "BCB" and "BCA". None of these are beautiful, so the answer is "Impossible".
2)	
    	
"XX"
Returns: "Impossible"
After removing one character you will get the string "X" that isn't beautiful. Please note that you have to remove exactly one character.
3)	
    	
"A"
Returns: "Impossible"
After removing one character you will get the empty string "". It isn't beautiful.
4)	
    	
"AABB"
Returns: "Possible"
You can get either "ABB" or "ABB". Both these strings are beautiful.
5)	
    	
"QWERTYY"
Returns: "Possible"
There are a few beautiful strings you can get. Some of them are "WERTYY" and "QWETYY".
6)	
    	
"ITHINKYOUAREAHUMAN"
Returns: "Impossible"
7)	
    	
"BOB"
Returns: "Possible"


'''


string="BCAB"
a=[]
for i in string:
    a.append(i)
#   print(a)
for i in range(len(a)-2):
    if(a[i]==a[i+2]):
        print("Beautiful string")
        del(a[i+1])
        print(a)
        break
    if(a[i]==a[i+1] and len(a)>2):
        print("Beautiful string")
        break

