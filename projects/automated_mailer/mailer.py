
import os
print(os.getcwd())

emails=[]
subject="test"
message=""

def execute():
    try:
        with open("data/email")as f:
            email=f.read()
            emails=email.split()

        with open("data/data")as f:
            message=f.read()
            
        
        for i in emails:
            os.system('echo "'+message+'" | mail -s "'+subject+'" '+i)
            print(i)
            
    except:
        print("Error opening files:")
        return

    
        
        
if __name__=="__main__":
    execute()

    

    
