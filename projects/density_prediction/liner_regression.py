from sklearn import linear_model
import pandas as pd
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import sklearn
import os
import matplotlib.pyplot as plt
from pandas import scatter_matrix

fig=plt.figure(figsize=(5,10))
fig.savefig('fig1.png', dpi = 300)
#       print(sklearn.__version__)
print(os.getcwd())

##############################################################################
#data loading

dataset=pd.read_csv('data/train.csv',index_col=None)
dataset2=pd.read_csv('data/test.csv',index_col=None)
#ddel(dataset[[0]])
#dataset.replace("?",0,inplace=True)
#print(dataset.columns)

##############################################################################
#data visualization

dataset.hist()
scatter_matrix(dataset)
plt.show()

dataset2.hist()
scatter_matrix(dataset2)
plt.show()

##############################################################################
# Print features type and describe them

print("\n\n -------------Dataset1 Description -------------------------------- \n\n")
print(dataset.describe())
print("\n\n -------------Data1 type Description---------------- \n\n")
print(dataset.dtypes)
print("\n\n -------------Dataset2 Description -------------------------------- \n\n")
print(dataset2.describe())
print("\n\n -------------Data2 type Description---------------- \n\n")
print(dataset2.dtypes)


##############################################################################
#Normalizing Data
scaler=StandardScaler()
dataset.iloc[:,0:-3]=StandardScaler().fit_transform(dataset.iloc[:,0:-3])
dataset2.iloc[:,0:-3]=StandardScaler().fit_transform(dataset2.iloc[:,0:-3])
#print(dataset)

##############################################################################
#Split training data into training and test set

train_x=dataset.iloc[:,0:-4]
test_x=dataset2.iloc[:,0:-4]
train_y=dataset.iloc[:,-1]
test_y=dataset2.iloc[:,-1]

print("\n\n -------------Test Train Split -------------------- \n\n")
print(train_x.shape)
print(test_x.shape)
print(train_y.shape)
print(test_y.shape)
print("\n\n --------------------------------------------- \n\n")

##############################################################################
#Train the model
model=linear_model.LinearRegression().fit(train_x,train_y)
print(model.coef_)
predict=model.predict(test_x)

############### ###############################################################
#Evaluation
print("Mean squared error:",mean_squared_error(test_y, predict))
print('R squared: %.2f' % r2_score(test_y, predict))
    
##############################################################################
'''


Co-efficeients : [ 11.61857509   3.87549961 -15.38578213  -9.6472152    0.97512855
   5.60822156  16.74080482 -14.26363287  14.38279232]
Mean squared error: 45.5699569709
R squared: 0.59


'''
