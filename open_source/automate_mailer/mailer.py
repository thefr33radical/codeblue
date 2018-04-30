
import os
print(os.getcwd())

l=[]
subject="test"
message=""

def execute():
    try:
        with open("data/email")as f:
            email=f.read()
            l=email.split()

        with open("data/data")as f:
            message=f.read()
            
        
        for i in l:
            os.system('echo "'+message+'" | mail -s "'+subject+'" '+i)
            print(i)
            
    except:
        print("Error opening files:")
        return

    
        
        
if __name__=="__main__":
    execute()

    

    