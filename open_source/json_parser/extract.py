'''


Script to convert nested json object to key value pairs
Contributors : Thefreeradical, Mahendra


Better optimized version using generators will be published soon.
Result JSON OBJECT to CSV or DATAFRAME can be converted in one more step.
 1. Remove commented lines to load key value pairs into dictionary obj
 2. Use pandas library to convert dictionary to dataframe
 3. Convert Datframe to CSV


'''    


import json
#obj=dict()
pathname="/home/kuliza287/Dynamic_Credit_Model/cibil_response.json"
def extract(key,value):
    if(type(value)==str):
        result = "{'"+key+"' : '"+value+"'}"
        print(result)
        #obj[key]=value
        return
        
    t = 0
    if(type(value)==list):
        for i in value:
            extract(key+"_"+str(t),i)
            t = t + 1
        return
        
    if(type(value)==dict):
        for i in value.keys():
            if key:
                key_i = key+"_"+i
            else:
                key_i = i
            extract(key_i,value[i])
        return
        
def compute():
    with open(pathname)as f:
        dat=f.read()
        json_data=json.loads(dat)
        d=dict(json_data)
        extract(None,d)        
        #print(obj)

if __name__=="__main__":
    compute()