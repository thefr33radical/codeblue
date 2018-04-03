import pandas as pd
from sklearn import svm
from pandas import scatter_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
dataset=pd.read_csv("model.csv")

###############################################################################
#Normalizing Data 

scaler=StandardScaler()
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
print(dataset.iloc[:int(0.2*len(dataset)),-1  ])
#dataset.iloc[:,:-2]=pd.DataFrame(StandardScaler().fit_transform(dataset.iloc[:,:-2]))
#

#dataset.columns=n
#print(dataset.head())

###############################################################################
#Split training data into training and test set
train_x=dataset.iloc[:int(0.8*len(dataset)),:-1]
test_x=dataset.iloc[int(0.8*len(dataset)):len(dataset),:-1]

train_x=StandardScaler().fit_transform(train_x)
test_x=StandardScaler().fit_transform(test_x)

train_y=dataset.iloc[:int(0.8*len(dataset)),-1]
test_y=(dataset.iloc[:int(0.2*len(dataset)),-1  ])
#print(type(train_y))
#print(train_x.head())
#print(test_y)

###############################################################################
#Model Training
model=svm.SVC(kernel="rbf")
z=model.fit(train_x,train_y)
#print(dataset.iloc[:,4])
#print(model.coef_)
pred=model.predict(test_x)
print('SVM score: %f'
      % z.score(test_x, test_y))
print("confusion matrix",confusion_matrix(test_y,pred))