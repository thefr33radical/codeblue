# your code goes here# your code goes hereimport json
import json
import pandas as pd
from sklean import linear_model
n = raw_input()
marks = []

for i in range(0,int(n)):
    dat=raw_input()
    dat=dat.replace(";","")
    dat=dat.replace("'",'"')
    #parse.unquote(dat.data())
    x=json.loads((dat))
    y=dict(x)
    #print y['m1']
    marks.append(y)

ide=[]
m1=[]
m2=[]
for i in marks:
    ide.append(i['id'])
    m1.append(i['m1'])
    m2.append(i['m2'])
    
df=pd.DataFrame({'col1':ide,'col2':m1,'col3':m2})
print df

#Y=[]
#model=linear_model.LinearRegression.fit(df,Y)
#print model.coef_


