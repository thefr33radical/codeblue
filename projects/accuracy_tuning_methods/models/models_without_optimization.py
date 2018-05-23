from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures as poly
import pandas as pd
import traceback
from sklearn import datasets


class Compute(object):

    def __init__(self):
        self.dataset = pd.DataFrame()
        self.train_x = pd.DataFrame()
        self.train_y = pd.DataFrame()
        self.test_x = pd.DataFrame()
        self.test_y = pd.DataFrame()
        self.path = ""

    def split_dataset(self):
        # Split training data into training and test set
        self.train_x = self.dataset.iloc[:-20 , :10]

        self.test_x = self.dataset.iloc[-20:, :10]
        self.train_y = self.dataset.iloc[:-20 ,-1]
        self.test_y = self.dataset.iloc[-20:, -1]

        return

    def data_loader(self):
        try:
            diabetes = datasets.load_diabetes()

            self.dataset=pd.DataFrame(diabetes["data"])
            self.dataset.columns=diabetes["feature_names"]
            target = pd.DataFrame( diabetes["target"], columns=["target"] )
            self.dataset = pd.concat( [ self.dataset, target], axis=1 )

            self.split_dataset()
            return (self.train_x, self.test_x, self.train_y,
                    self.test_y)
        except Exception:
            traceback.print_exc()
            return (None, None, None, None)


class Algorithms(object):

    def __init__(self, model_name, train_x, test_x, train_y, test_y):

        if model_name  =="elasticnet":
            self.elasticnet(model_name, train_x, test_x, train_y, test_y)

        if model_name == "svr":
            self.svr(model_name, train_x, test_x, train_y, test_y)

        if model_name == "linear":
                self.linear(model_name, train_x, test_x, train_y, test_y)

        if model_name == "polynomial":
            self.polynomial(model_name, train_x, test_x, train_y, test_y)

        if model_name == "lasso":
            self.lasso(model_name, train_x, test_x, train_y, test_y)

    def svr(self, model_name, train_x, test_x, train_y, test_y):
        model = svm.SVR(kernel='rbf')
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name,train_y,train_x,test_y,pred, model )

    def polynomial(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.LinearRegression()
        temp = poly(degree=2)
        train_x_poly = temp.fit_transform(train_x)
        test_x_poly = temp.fit_transform(test_x)

        model2 = model.fit(train_x_poly, train_y)
        pred2 = model2.predict(test_x_poly)
        self.print_score(model_name, train_y, train_x, test_y, pred2, model )

    def linear(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.LinearRegression()
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name,train_y,train_x,test_y,pred, model )

    def ridge(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.Ridge(alpha=3)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name,train_y,train_x,test_y,pred, model )

    def lasso(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.Lasso()
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name,train_y,train_x,test_y,pred, model)

    def elasticnet(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.ElasticNet(alpha=1)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        #print(pred)
        self.print_score( model_name,train_y,train_x,test_y,pred, model )

    def print_score(self, model_name, train_y, train_x, test_y, pred, model):
        try:
            print(len(pred),len(test_y))
            print(model_name+" Mean Squared Error: ", mean_squared_error(test_y, pred))
            print(model_name+" R2 Score : ", r2_score(test_y, pred))
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    obj = Compute()
    (train_x, test_x, train_y, test_y) = obj.data_loader()
    #print(len(train_x), len(train_y), len(test_x), len(test_y))
    obj2 = Algorithms("elasticnet", train_x, test_x, train_y, test_y)

    ''' TEST CASES
    obj2 = Algorithms("svr", train_x, test_x, train_y, test_y)
    obj2 = Algorithms("lasso", train_x, test_x, train_y, test_y)
    obj2 = Algorithms("linear", train_x, test_x, train_y, test_y)
    obj2 = Algorithms("polynomial", train_x, test_x, train_y, test_y)
    '''


        

