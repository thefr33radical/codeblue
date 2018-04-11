'''

1. Change file name to your own, under data directory.
2. generate key from the site textbelt
3. Uncomment lines related to dataset dataframe
4. Not meant for commercial use, just a L1 project

Author : thefr33radical

'''


import requests
import pandas as pd

url='https://textbelt.com/text'

#Data is stored in a csv file of  \ Phone Number \ Message \
filename="/data/file.csv"

#generate your own key @ textbelt.com
key=""

def compute():
    #dataset=pd.read_csv(filename,header=None)
    #numbers=dataset[0]
    #message=dataset[1]
    numbers=['0000000000']
    message=['Hello World']

    for i in range(len(numbers)):
        num=numbers[i]
        m=message[i]
        body={  'phone': num,  'message': m,  'key':key}
        #print(num,m)
        try:
            r=requests.post(url,body)
            if(r.status_code==requests.codes.ok):
                print("success")
            else:
                print("error sending message")
        except:
            pass
            


if __name__=="__main__":
    compute()