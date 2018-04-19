import pandas as pd
from sklearn.preprocessing import StandardScaler as s

dataset=pd.read_csv("data/cancer.csv")

cancer_type=dataset.iloc[:,-1:]
cancer_features=dataset.iloc[:,:-1]

cancer_type=s.fit().transform(cancer_type)
print(cancer_type)


