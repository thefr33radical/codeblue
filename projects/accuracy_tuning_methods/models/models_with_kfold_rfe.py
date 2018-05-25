from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures as poly
import pandas as pd
import traceback
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
from sklearn.cross_validation import cross_val_score
import numpy as np
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
        self.train_x = self.dataset.iloc[:-5, :10]

        self.test_x = self.dataset.iloc[-5:, :10]
        self.train_y = self.dataset.iloc[:-5, -1]
        self.test_y = self.dataset.iloc[-5:, -1]

        print(self.train_x.iloc[:,-2])

        return

    def data_loader(self):
        try:
            diabetes = datasets.load_diabetes()

            self.dataset = pd.DataFrame(diabetes["data"])
            self.dataset.columns = diabetes["feature_names"]
            target = pd.DataFrame(diabetes["target"], columns=["target"])
            self.dataset = pd.concat([self.dataset, target], axis=1)

            self.split_dataset()
            return (self.train_x, self.test_x, self.train_y,
                    self.test_y)
        except Exception:
            traceback.print_exc()
            return (None, None, None, None)


class Algorithms(object):

    def __init__(self, model_name, train_x, test_x, train_y, test_y):

        if model_name == "elasticnet":
            self.elasticnet(model_name, train_x, test_x, train_y, test_y)

        if model_name == "svr":
            self.svr(model_name, train_x, test_x, train_y, test_y)

        if model_name == "linear":
            self.linear(model_name, train_x, test_x, train_y, test_y)

        if model_name == "polynomial":
            self.polynomial(model_name, train_x, test_x, train_y, test_y)

        if model_name == "lasso":
            self.lasso(model_name, train_x, test_x, train_y, test_y)



        '''   def rfe(self, train_x, test_x, train_y, test_y):
        final_error = 999999
        count_of_features = len(train_x.columns)
        n_features = []
        feature_rank = []
        temp_train_x = []
        temp_test_x = []

        models = [RandomForestRegressor(), linear_model.LinearRegression()]
        model_name = ""

        for model in models:
            for i in range(1, count_of_features):
                selector = PCA(n_components=i)
                selector = selector.fit(train_x, train_y)

                temp_pred = selector.transform(test_x)
                self.polynomial("polynomial",train_x,test_x,train_y, test_y)
                
        return train_x, test_x '''

    def pca(self, train_x, test_x, train_y, test_y):
        pass



    def rfe(self, train_x, test_x, train_y, test_y):
        final_error = 999999
        count_of_features = len(train_x.columns)
        n_features=[]
        feature_rank=[]
        temp_train_x=[]
        temp_test_x=[]

        models = [RandomForestRegressor(), linear_model.LinearRegression()]
        model_name=""

        for model in models:
            for i in range(1, count_of_features):
                selector = RFE(model, i, step=1)
                selector = selector.fit(train_x, train_y)

                temp_pred = selector.predict(test_x)
                mean_error = mean_squared_error(test_y, temp_pred)

                if mean_error < final_error:
                    final_error = mean_error
                    model_name=str(model)
                    n_features=selector.n_features_
                    feature_rank=selector.ranking_
                    temp_train_x=selector.transform(train_x)
                    temp_test_x=selector.transform(test_x)
        print("Feature Mean error: ", final_error, n_features, feature_rank)
        feature_labels=list(zip(feature_rank, train_x.columns))
        feature_labels_rank=[]
        count=0
        for i in feature_labels:
            temp=list(i)
            temp.append(count)
            feature_labels_rank.append(temp)
            count+=1

        feature_rank=pd.DataFrame(feature_labels_rank,columns=["Rank","Label","Index"])
        #feature_rank.to_csv("feature_rank.csv")
        print(feature_rank)

        test_x=pd.DataFrame(temp_test_x)
        train_x=pd.DataFrame(temp_train_x)
        #print(test_x)
        return train_x, test_x

    def svr(self, model_name, train_x, test_x, train_y, test_y):
        model = svm.SVR(kernel='rbf')
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)

        self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def compute_score(self, test_y, pred):
         return r2_score(test_y, pred), mean_squared_error(test_y, pred)

    def polynomial(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.LinearRegression()

        models = [RandomForestRegressor(), linear_model.LinearRegression(), svm.SVR(kernel='rbf'), linear_model.Ridge(alpha=3), linear_model.ElasticNet(alpha=1)]

        count_of_features = len(train_x.columns)

        global_r2_score=9999999
        global_mean_score=999999

        for model in models:
            for i in range(1, count_of_features):
                selector = PCA(n_components=i)
                selector.fit(train_x, train_y)

                temp_train_x = selector.transform(train_x)
                temp_test_x = selector.transform(test_x)

                model_name=str(model)
                model.fit(temp_train_x ,train_y)
                pred = model.predict(temp_test_x)
                scores = cross_val_score(model,temp_train_x, train_y, scoring="neg_mean_squared_error", cv=25)
                rmse_scores = np.sqrt(-scores)

                print(" Cross RMSE : ",max(rmse_scores), "Model name : ",model_name[:5], "  Dimensions : ",  i, " RMSE : ",np.sqrt(mean_squared_error(test_y,pred)), " R2 Score :", r2_score(test_y,pred) )

                #r2_score,mean_squared_error=self.compute_score(test_y, pred)


                #self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def linear(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.LinearRegression()
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x,train_y)
        pred=model.predict(test_x)
        self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def ridge(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.Ridge(alpha=3)
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def lasso(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.Lasso()
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def elasticnet(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.ElasticNet(alpha=1)
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def print_score(self, model_name, train_y, train_x, test_y, pred, model):
        try:
            print(len(pred), len(test_y))
            print(model_name + " Mean Squared Error: ", mean_squared_error(test_y, pred))
            print(model_name + " R2 Score : ", r2_score(test_y, pred))
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    obj = Compute()
    (train_x, test_x, train_y, test_y) = obj.data_loader()
    # print(len(train_x), len(train_y), len(test_x), len(test_y))
    obj2 = Algorithms("liner", train_x, test_x, train_y, test_y)
    obj2.polynomial("linear", train_x, test_x, train_y, test_y)

    ''' TEST CASES
    
    '''




