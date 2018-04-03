import pandas as pd
from sklearn import linear_model
from pandas import scatter_matrix
from sklearn.preprocessing import StandardScaler
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder
dataset=pd.read_csv("dataset.csv")

##############################################################################
# Label Encoding - converting to nominal values

dataset["purfloan"]=LabelEncoder().fit_transform(dataset["purpOfloan"].astype(str))
dataset["loape"]=LabelEncoder().fit_transform(dataset["loape"].astype(str))
dataset["organo"]=LabelEncoder().fit_transform(dataset["organiType"].astype(str))
dataset["regionFrcode"]=LabelEncoder().fit_transform(dataset["regionode"].astype(str))
dataset["homePremises"]=LabelEncoder().fit_transform(dataset["hoises"].astype(str))
dataset["initissAge"]=LabelEncoder().fit_transform(dataset["initige"].astype(str))
dataset["emplnce"]=LabelEncoder().fit_transform(dataset["emplnce"].astype(str))
dataset["resince"]=LabelEncoder().fit_transform(dataset["rece"].astype(str))
dataset["overaience"]=LabelEncoder().fit_transform(dataset["overience"].astype(str))
dataset["orgpe"]=LabelEncoder().fit_transform(dataset["orgaType"].astype(str))

dataset["currenion"].replace('([a-zA-Z ]+)', "1", regex=True,inplace=True)
dataset["loate"].replace('((.*)[-]+(.*))', "1", regex=True,inplace=True)
#dataset["dealerI"]=(dataset["currentOrganisation"].astype(float))
#dataset["cibilScore"]=(dataset["cibilScore"].astype(int))

dataset =dataset[dataset['inimi'].apply(lambda x: x.isdigit())]
dataset["ilEmi"]=(dataset["imi"].astype(float))

dataset =dataset[dataset['loMax'].apply(lambda x: x.isdigit())]
dataset["loMax"]=(dataset["loax"].astype(float))

dataset =dataset[dataset['cire'].apply(lambda x: x.isdigit())]
dataset["ccore"]=(dataset["cire"].astype(float))

dataset =dataset[dataset['dea'].apply(lambda x: x.isdigit())]
dataset["ded"]=(dataset["dead"].astype(float))

dataset =dataset[dataset['organisati'].apply(lambda x: x.isdigit())]
dataset["organisat"]=(dataset["organisa"].astype(float))

dataset =dataset[dataset['currensation'].apply(lambda x: x.isdigit())]
dataset["isation"]=(dataset["ation"].astype(float))

#dataset =dataset[dataset['loanSanctionDate'].apply(lambda x: x.isdigit())]
dataset["nctionDate"]=(dataset["onDate"].astype(float))

dataset.to_csv("model.csv")
##############################################################################
# Print features type and describe them

print("\n\n -------------Dataset1 Description -------------------------------- \n\n")
print(dataset.describe())
print("\n\n -------------Data1 type Description---------------- \n\n")
print(dataset.dtypes)
#print("\n\n -------------Dataset2 Description -------------------------------- \n\n")


#dataset["isation"]=LabelEncoder().fit_transform(dataset["n"].astype(str))  
#print(dataset["loannDate"])