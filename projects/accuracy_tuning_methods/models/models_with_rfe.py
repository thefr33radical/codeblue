from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures as poly
import pandas as pd
import numpy as np
import traceback
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.decomposition import PCA


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

    def rfe_model(self, train_x, test_x, train_y, test_y):
        final_error = 999999
        count_of_features = len(train_x.columns)
        n_features = []
        feature_rank = []
        temp_train_x = []
        temp_test_x = []

        models = [RandomForestRegressor(), linear_model.LinearRegression()]
        for model in models:
            for i in range(1, count_of_features):
                selector = RFE(model, i, step=1)
                selector = selector.fit(train_x, train_y)

                temp_pred = selector.predict(test_x)
                mean_error = mean_squared_error(test_y, temp_pred)

                if mean_error < final_error:
                    final_error = mean_error
                    n_features = selector.n_features_
                    feature_rank = selector.ranking_
                    temp_train_x = selector.transform(train_x)
                    temp_test_x = selector.transform(test_x)
        print("Feature Mean error: ", final_error, n_features, feature_rank)
        feature_labels = list(zip(feature_rank, train_x.columns))
        feature_labels_rank = []
        count = 0
        for i in feature_labels:
            temp = list(i)
            temp.append(count)
            feature_labels_rank.append(temp)
            count += 1

        feature_rank = pd.DataFrame(feature_labels_rank, columns=["Rank", "Label", "Index"])
        feature_rank.to_csv("feature_rank.csv")
        print(feature_rank)

        test_x = pd.DataFrame(temp_test_x)
        train_x = pd.DataFrame(temp_train_x)
        # print(test_x)
        return train_x, test_x



    def svr(self, model_name, train_x, test_x, train_y, test_y):
        model = svm.SVR(kernel='rbf')
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(model_name, train_y, train_x, test_y, pred, model)

    def polynomial(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.LinearRegression()

        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)

        temp = poly(degree=2)
        train_x_poly = temp.fit_transform(train_x)
        test_x_poly = temp.fit_transform(test_x)

        model2 = model.fit(train_x_poly, train_y)
        pred2 = model2.predict(test_x_poly)
        self.print_score(model_name, train_y, train_x, test_y, pred2, model)

    def linear(self, model_name, train_x, test_x, train_y, test_y):
        model = linear_model.LinearRegression()
        train_x, test_x = self.rfe(train_x, test_x, train_y, test_y)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
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
    obj2 = Algorithms("linear", train_x, test_x, train_y, test_y)
    #obj2 = Algorithms()



    ''' TEST CASES
    obj2.pca_model(train_x, test_x, train_y, test_y)
    obj2.rfe_model(train_x, test_x, train_y, test_y)

    '''




