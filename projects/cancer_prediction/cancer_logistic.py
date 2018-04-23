import pandas as pd
from sklearn.preprocessing import StandardScaler as s

dataset=pd.read_csv("data/cancer.csv")

cancer_type=dataset.iloc[:,-1:]
cancer_features=dataset.iloc[:,:-1]

scaler=s(copy=True, with_mean=True, with_std=True)
f=scaler.fit_transform(cancer_features)

#y= lambda x:  i+x for i in scaler.mean_

#print(y)




