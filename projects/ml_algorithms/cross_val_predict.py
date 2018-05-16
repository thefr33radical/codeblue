from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import cross_val_predict

db=datasets.load_diabetes()
model=linear_model.LinearRegression()
x=db.data[:150]
y=db.target[:150]
pred=cross_val_predict(model,x,y)


print(x,y)
print(len(datasets.__all__))
    