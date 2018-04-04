'''

txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
        
   
     '''
import re        
        
def compute():
    
    
    txt= "THIS IS A TEST TEXT TEST"
    pat = "TEST"
    m = re.search(pat, txt)
    print(m.span())
    if pat in txt:
       print("yes")
        


if __name__=="__main__":
    compute()