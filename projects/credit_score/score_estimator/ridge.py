
import pandas as pd
from sklearn import linear_model
#from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures as p
from pandas import scatter_matrix
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import os
print(os.getcwd())
##############################################################################
#data loading

n=["Status of existing checking account","Duration in month","Credit history","Purpose","Credit amount","Savings account/bonds","Present employment since","Installment rate","Personal status and sex","Other debtors guarantors ","Present residence since ","Property ","Age in years ","Other installment plans ","Housing ","Number of existing credits at this bank","Job","Number of people being liable to provide maintenance","Telephone ","foreign worker"]
dataset=pd.read_csv('dataset/german_credit_datset/german.data-numeric.txt',index_col=None,names=n,sep="  ")


#dataset2=pd.read_csv('data/test.csv',index_col=None)
#ddel(dataset[[0]])
#dataset.replace("?",0,inplace=True)
#print(dataset)
#print(len(names),dataset.columns)
#dataset.rename(columns=names,inplace=True)

###############################################################################
# Label Encoding

#dataset["col"]=LabelEncoder().fit_transform(dataset["col"].astype(str))

##############################################################################
# Print features type and describe them

#dataset=dataset[[i for  i in n]].astype(float)
dataset.fillna(0,inplace=True)
'''
print("\n\n -------------Dataset1 Description--------------------------- \n\n")
print(dataset.describe(include='all'))
print("\n\n -------------Data1 type Description---------------- \n\n")
print(dataset.dtypes)
'''
###############################################################################
#data visualization
#
#print(plt.matshow(dataset.corr()))
#dataset.hist()
#scatter_matrix(dataset)
#plt.show()

###############################################################################
#Normalizing Data 

scaler=StandardScaler()
dataset=pd.DataFrame(StandardScaler().fit_transform(dataset))
#print(plt.matshow(dataset.corr()))
#dataset.columns=n
#print(dataset.head())

###############################################################################
#Split training data into training and test set
train_x=dataset.iloc[:int(0.8*len(dataset)),:4]
train_x.append(dataset.iloc[:int(0.8*len(dataset)),5:])
test_x=dataset.iloc[int(0.8*len(dataset)):len(dataset),:4]
test_x.append(dataset.iloc[int(0.8*len(dataset)):len(dataset),6:])

train_y=dataset.iloc[:int(0.8*len(dataset)),4]
test_y=(dataset.iloc[:int(0.2*len(dataset)),4])
print(type(train_y))
#print(train_x.head())
#print(train_x,test_x)

###############################################################################
#Model Training
model=linear_model.Ridge(alpha=3)
model.fit(train_x,train_y)
#print(dataset.iloc[:,4])
#print(model.coef_)
pred=model.predict(test_x)



###############################################################################
print("Mean squared error:",mean_squared_error(test_y, pred))
print('R squared: %.2f' % r2_score(test_y, pred))

