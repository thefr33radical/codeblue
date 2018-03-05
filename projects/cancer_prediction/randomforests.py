# Random forest algortihm implementation using D=Sklearn
#dataset : UCI Cancer dataset (attached)
#Purpose : Exploration

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import sklearn
import os
import numpy as np
#       print(sklearn.__version__)
print(os.getcwd())

#Data Loading

##############################################################################

dataset=pd.read_csv('data/cancer.txt',sep=",",header=None,index_col=None)
#ddel(dataset[[0]])
dataset.replace("?",0,inplace=True)
dataset.columns=["CodeNumber", "ClumpThickness", "UniformityCellSize", "UniformityCellShape", "MarginalAdhesion",
              "SingleEpithelialCellSize", "BareNuclei", "BlandChromatin", "NormalNucleoli", "Mitoses",
  "CancerType"]
#a=np.arange(0,1000,1)
#a=list(a)
#
#for i in dataset['BareNuclei']:
#    if(int(i) not in a):
#        print(i)
       # pass
dataset.to_csv("data/cancer.csv",index=False)

##############################################################################

# Print features type and describe them
dataset['BareNuclei']=dataset['BareNuclei'].astype(int)
#print(dataset['BareNuclei'].describe())
#print(dataset.dtypes)

##############################################################################

#Split training data into training and test set
#print(dataset.iloc[:,-1])
train_x,test_x,train_y,test_y=train_test_split(dataset.iloc[:,0:-1],dataset.iloc[:,-1],train_size=0.8)
print(train_x.shape)
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)

##############################################################################

#Training & Testing the model using RandomForestClassifier

model=RandomForestClassifier(criterion='gini').fit(train_x,train_y)
print(model)
predict_model=model.predict(test_x)

##############################################################################

#Accuracy score

print("Accuracy Score : ", accuracy_score(train_y,model.predict(train_x)))
print("Accuracy Score : ", accuracy_score(test_y,model.predict(test_x)))


###############################################################################
if __name__=='__main__':
    print("exiting")

