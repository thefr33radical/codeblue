import re
class book:
    def __init__(self):
        self.bookid=0
        self.title=""
        self.authorid=0   
        self.cat=""
        self.sold=0
        
        
class author:
    def __init__(self):
        self.authorid=0
        self.name=""
        
        
class book_catalog:
    def __init__(self):
        self.author_list=list()
        self.book_list=list()
        
    def add_author(self,author_obj):
        self.author_list.append(author_obj)
        
    def add_book(self,book_obj):
        self.book_list.append(book_obj)
        
    def get_category(self):
        temp=[]
        for i in self.book_list:
            temp.append(i.cat)
        
        temp=set(temp)
        print(temp)
        
    def get_author(self):
        temp=[]
        for i in self.author_list:
            temp.append(i.name)
        
        temp=set(temp)
        print(temp)
        
    def get_sold(self):
        minimum=self.book_list[0].sold
        temp_bookid=self.book_list[0].bookid
        temp_title=self.book_list[0].title
        temp_authorid=self.book_list[0].authorid
        temp_cat=self.book_list[0].cat
        
        for i in range(1,len(self.book_list)):
            if(minimum>=self.book_list[i].sold):
                minimum=self.book_list[i].sold
                temp_bookid=self.book_list[i].bookid
                temp_title=self.book_list[i].title
                temp_authorid=self.book_list[i].authorid
                temp_cat=self.book_list[i].cat
                
        print(temp_bookid,temp_title,temp_authorid,temp_cat,minimum)
                
    def search(self,text):
        for i in self.book_list:
            matchObj = re.match( r'(.*)'+text+'(.*?) .*', i.title, re.M|re.I)
            if(matchObj):
                print(matchObj.group())
                
        for i in self.author_list:
            #print(i.name)
            matchObj = re.match( r'(.*)'+text+'(.*?) .*', i.name, re.M|re.I)
            if(matchObj):
                print(matchObj.group())
                
        
            
if __name__=="__main__":
    c=book_catalog()
    while(1):
        print(" 1.insert book 2.insert author 3.get author 4. get category 5. get most sold 6.search 7. exit \n \n")
        inp=input()
        if(int(inp)==1):
            b=book()
            print("insert bookid\n")
            temp=input()
            b.bookid=int(temp)
            print("insert title\n")
            temp=input()
            b.title=temp
            print("insert authorid\n")
            temp=input()
            b.authorid=int(temp)
            print("insert category\n")
            temp=input()
            b.cat=str(temp)
            print("insert sold count\n")
            temp=input()
            b.sold=int(temp)
            c.add_book(b)
            
        elif(int(inp)==2):
            a=author()
            print("insert authorid")
            temp=input()
            a.authorid=int(temp)
            print("insert name")
            temp=input()
            a.name=temp
            c.add_author(a)
            
        if(int(inp)==3):
            c.get_author()
            
        if(int(inp)==4):
            c.get_category()
            
        if(int(inp)==5):
            c.get_sold()
            
        if(int(inp)==6):
            print("enter partial text")
            temp=input()
            c.search(temp)
        if(int(inp)==7):
            break
        
        else:
            print("Please enter proper input")
        