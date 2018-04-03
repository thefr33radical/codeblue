import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from pandas import scatter_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

dataset=pd.read_csv("model.csv")

###############################################################################
#Normalizing Data 
print(dataset.hist())
scaler=StandardScaler()
#print(dataset.iloc[:int(0.2*len(dataset)),-1  ])
#plt.rcParams["figure.figsize"] = [50,50]
#print(plt.matshow(dataset.corr()))
#plt.savefig('feature_hist.png')

#plt.rcParams["figure.figsize"] = [50,50]
#print(plt.matshow(dataset.corr()))
#plt.savefig('feature_correlation.png')

#dataset.columns=n
#print(dataset.head())

###############################################################################
#Split training data into training and test set
train_x=dataset.iloc[:int(0.8*len(dataset)),:-1]
test_x=dataset.iloc[int(0.8*len(dataset)):len(dataset),:-1]


train_x=StandardScaler().fit_transform(train_x)
test_x=StandardScaler().fit_transform(test_x)


train_y=dataset.iloc[:int(0.8*len(dataset)),-1]
test_y=(dataset.iloc[int(0.8*len(dataset)):len(dataset),-1  ])
#print(type(train_y))
#print(train_x.head())
#print(test_y)

###############################################################################
#Model Training
model=RandomForestClassifier()
z=model.fit(train_x,train_y)
#print(dataset.iloc[:,4])
#print(model.coef_)
pred=model.predict(test_x)
print('RandomForestClassifier score: %f'
      % z.score(test_x, test_y))
      
print("confusion matrix",confusion_matrix(test_y,pred))
#dataset.iloc[:,:].value_counts().plot(kind='bar')