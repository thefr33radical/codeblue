#from pyparsing import *
#mport argparse, subprocess
import json, csv
import pandas as pd
import re
import numpy as np 
from io import StringIO
from pandas.io.json import json_normalize
import ast 

obj=dict()

pathname="/home/kuliza227/Downloads/loc.txt"
def extract(key,value,temp):

    if (type(value) == dict):

        for key, val in value.items():
            if (type(val) is str):
                temp[key] = val




        for i in value.keys():
            if key:
                key_i = key + "_" + i
            else:
                key_i = i
            # print("i am")
            extract(key_i, value[i], temp)
            temp.clear()
        return

        # t = 0
    elif (type(value) == list):
            for i in value:
                extract(key, i, temp)
                # counter = counter - 1
                # t = t + 1

            return

    elif(type(value)==str):
        result =key+": "+value

        obj[key]=obj.get(key,[]) + [ value ]
        obj_keys=obj.keys()

        print(temp)

        for i,j in temp.items():
            obj[i]=[j]
        #print(obj)

        #obj[key]=value
        s=StringIO(result)
        with open('outexcel.txt', 'a+') as f:
          for line in s:
            f.write(line +",")

        return
        

    

def compute():
    with open(pathname)as f:
        dat=f.read()  
        json_data=json.loads(dat)
        d=dict(json_data)
        extract(None,d,dict())
        #d1=json_normalize(d)
        #print(obj) 
        columns=list(obj.keys());
        values = list(obj.values());
        arr_len = len(values)
        #print(values)
        with open('outexcel.txt', 'r') as myfile :
             data=myfile.read()
        myfile.close()
        #print(obj)
        #data=data.decode()
        #data = '"' + data +'"'
        #d1 =ast.literal_eval(data) #has the dictionary format
        #d1 = {k:v for k,v in (x.split(':') for x in data) }
        #print(d1)       
        #d2=eval(d1)
        df=pd.DataFrame.from_dict(obj,orient='index')
        print(df)
        df= df.transpose() 
        #print(df)   
        #from_dict = pd.DataFrame({k: [v] for (k, v) in obj.items()})        
        #df = pdgg.concat([df, from_dict]) #default axis = 0
        #df=pd.DataFrame(np.array(values, dtype=object).reshape(-1,arr_len), columns=columns)
        #print(df)
        #df = pd.read_fwf(StringIO(data)).to_dict()
        #df = pd.read_fwf('./outexcel.txt').to_dict()
        #print(df)
        #df1=pd.Series(df).reset_index()
        #df1=pd.DataFrame(df) 
        #print(df1)
        df.to_csv('outexcel.csv')
        #d1=dict(map(int, x.split(':')) for x in list)
        #print(d1)
        #with open('outexcel.csv', 'w') as f:
        #    writer =csv.DictWriter(f,lineterminator='\n',fieldnames=columns)
        #    writer.writeheader()
        #    writer.writerows(d1)
 
        df = pd.read_csv('outexcel.csv')


if __name__=="__main__":
    compute()