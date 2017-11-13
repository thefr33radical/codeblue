from sklearn.externals.joblib import Memory
from sklearn.datasets import load_svmlight_file
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import numpy as np
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import os
from sklearn.datasets import load_files
import glob
import sys
import re
import pickle
import os
import sys

path_name=os.path.abspath(os.path.dirname(sys.argv[0]))
filename=("model.sav")

#load tarining files
subset = load_files(path_name+'/aclImdb/train',shuffle='False',encoding='utf-8')
#load testing files
subset2=load_files(path_name+'/aclImdb/test',shuffle='False',encoding='utf-8')
'''load files format:
{
'DESCR': None,
 'data': [],
 'filenames': array(),
 'target': array(),
 'target_names': []
}

Since target values of the dataset are stored in file name. We extract it. For more info read dataset info.
'''

for i in range(0,len(subset.data)):

    f_name=subset.filenames[i]
    #print(f_name)
    temp=f_name.split("_")
    temp2=temp[2].split(".")
    #print(temp2)
    #subset.target[i]=temp2[0]
  #  print((subset.data[i]), subset.filenames[i],subset.target[i])
    
#  We do the same with testing set.
for i in range(0,len(subset2.data)):
    f_name=subset2.filenames[i]
    temp=f_name.split("_")
    temp2=temp[2].split(".")
    subset2.target[i]=temp2[0]
    
# extract count features (this transforms to a vocabularyXsentence [count matrix])
v=CountVectorizer()
X=v.fit_transform(subset.data)
#print(v.get_feature_names())

#train the model using Multinomial Naive bayes since score is in range 0-9
model=MultinomialNB()
model.fit(X,subset.target)
#save the model 
pickle.dump(model,open(filename,"wb"))


#--------------------------Testing-------------------------------------------------------
    
model=pickle.load(open(filename,"rb"))
X2=v.transform(subset2.data)
expected=subset2.target
predicted=model.predict(X2)

c=pd.DataFrame({'test_data':subset2.data,'actual_value':subset2.target,'predicted':predicted})
c.to_csv("output.csv")

l=['this is very good.',
                'this is bad.',
                'this is very bad.',
                'this is not good.',    
                'this is not what i had expected.',
                'you are taking too much time.',
                'this is good',
                'this is awesome',
                'this is slighly good',
                'i expected better than this',
                'this is much more than my expectation',
                'this is something i love',
                'this is something i hate',
                 
                'you are taking a hell lot of time.']
                
X3=v.transform(l)
predicted2=model.predict(X3)

c2=pd.DataFrame({'test_data':l,'predicted':predicted2})
c2.to_csv("output2.csv")

report=(metrics.classification_report(expected, predicted))
con_matrix=(metrics.confusion_matrix(expected, predicted))


print(report,con_matrix)
#with open("report.txt","w+") as f:
   # f.write(report)
   # f.write(con_matrix)
    
















