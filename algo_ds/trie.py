
# trie implementation in Python
#T(O) Searching : O(m) where m is the length of the string
#S(O) 26 X length of the key M X Number of keys N
 
class node(object):
    def __init__(self):
        self.kids=[0 for i in range(26)]
        self.pointer=[None for i in range(1,26)]
        self.isleaf=False

class trie(object):
      
     def __init__(self,v):
        self.head=v
        self.words_list=[]
        
        
     def insert_word(self,words):
         print("inserting")
         temp=self.head
         v=""
         index=0
         if(not temp):
             return
         for i in words:
                index=ord(i)-ord('a')
                if(temp.kids[index]==0):
                    temp.kids[index]=1
                    temp.pointer[index]=node()
                    #print("letters:",i)
                    v=v+i
                    temp=temp.pointer[index]
         self.words_list.append(v)
         print(self.words_list)
                    
     def bfs_search(self,temp,val,words):
            if(temp):
             words+=chr(val+ord('a'))
            # print(words)
             leafcount=0
             for i in  range(len(temp.pointer)):
                if(temp.pointer[i]):
                    leafcount+=1
                    val=i
                  #  print(chr(i+ord('a')),words)
                    self.bfs_search(temp.pointer[i],i,words)
                  
             if(leafcount==0):
                temp.isleaf=True
               # print(chr(val+ord('a')),words,temp.isleaf)
               #print(self.words_list)
                return 
             else:
               #  print(chr(val+ord('a')),words,temp.isleaf)
                 return
                 
     def print_words(self):
        temp=self.head
       # print(temp)
        if (not temp):
            print("no head")
            return
        #print("prining")
        for i in range(len(temp.pointer)):
            if(temp.pointer[i]):
                #   words_list[j]=ord(temp[i].kids)+ord('a')
                self.bfs_search(temp.pointer[i],i,"")
     #   print(words_list)

  
a=node()
obj=trie(a)
obj.insert_word("gowtham")
obj.print_words()
obj.insert_word("krishna")
obj.print_words()
obj.insert_word("midhun")
obj.print_words()
obj.insert_word("akshita")
obj.print_words()

  
            