from sklearn import svm
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures as poly
import traceback
import pandas as pd

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
        self.train_x = self.dataset.iloc[:int(0.8 * len(self.dataset)),
                                         :4]
        self.train_x.append(self.dataset.iloc[:int(0.8
                                                   * len(self.dataset)), 5:])
        self.test_x = self.dataset.iloc[int(0.8 * len(self.dataset)):
                                        len(self.dataset), :4]
        self.test_x.append(self.dataset.iloc[int(
            0.8 * len(self.dataset)):len(self.dataset), 6:])
        self.train_y = self.dataset.iloc[:int(0.8 * len(self.dataset)),
                                         4]
        self.test_y = self.dataset.iloc[:int(0.2 * len(self.dataset)),
                                        4]
        print (self.train_x, self.test_x, self.train_y, self.test_y)
        return

   
    def data_loader(self):
        try:
            self.path = input()
            self.dataset = pd.read_csv(
                self.path,
                index_col=None,
                names= [
                'Status of existing checking account',
                'Duration in month',
                'Credit history',
                'Purpose',
                'Credit amount',
                'Savings account/bonds',
                'Present employment since',
                'Installment rate',
                'Personal status and sex',
                'Other debtors guarantors ',
                'Present residence since ',
                'Property ',
                'Age in years ',
                'Other installment plans ',
                'Housing ',
                'Number of existing credits at this bank',
                'Job',
                'Number of people being liable to provide maintenance',
                'Telephone ',
                'foreign worker',
                ],
                sep='  ',
                engine="python")
            # visual=proc.Process(target=self.data_visualization)
            # visual.start()
            # self.data_preprocessing()
            
            self.split_dataset()

            return (self.train_x, self.test_x, self.train_y,
                    self.test_y)
        except Exception:
            traceback.print_exc()
            return (-1, -1, -1, -1)


class Algorithms(object):
    
    def __init__(self,
        model_name,
        train_x,
        train_y,
        test_x,
        test_y):
        self.elasticnet(model_name,
        train_x,
        train_y,
        test_x,
        test_y)
        
        self.svr(model_name,
        train_x,
        train_y,
        test_x,
        test_y)
        
        self.linear(model_name,
        train_x,
        train_y,
        test_x,
        test_y)
        
        self.polynomial(model_name,
        train_x,
        train_y,
        test_x,
        test_y)
        
        self.lasso(model_name,
        train_x,
        train_y,
        test_x,
        test_y)
        

    def svr(
        self,
        model_name,
        train_x,
        test_x,
        train_y,
        test_y,
    ):
        model = svm.SVR(kernel='rbf')
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(
            model_name,
            train_y,
            train_x,
            test_y,
            pred,
            model,
        )

    def polynomial(
        self,
        model_name,
        train_x,
        test_x,
        train_y,
        test_y,
    ):
        model = linear_model.LinearRegression()
        temp = poly(degree=2)
        train_x_poly = temp.fit_transform(train_x)
        test_x_poly = temp.fit_transform(test_x)

        model2 = model.fit(train_x_poly, train_y)
        pred2 = model2.predict(test_x_poly)
        self.print_score(
            model_name,
            train_y,
            train_x_poly,
            test_y,
            pred2,
            model2,
        )

    def linear(
        self,
        model_name,
        train_x,
        test_x,
        train_y,
        test_y,
    ):
        model = linear_model.LinearRegression()
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(
            model_name,
            train_y,
            train_x,
            test_y,
            pred,
            model,
        )

    def ridge(
        self,
        model_name,
        train_x,
        test_x,
        train_y,
        test_y,
    ):
        model = linear_model.Ridge(alpha=3)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(
            model_name,
            train_y,
            train_x,
            test_y,
            pred,
            model,
        )

    def lasso(
        self,
        model_name,
        train_x,
        test_x,
        train_y,
        test_y,
    ):
        model = linear_model.Lasso()
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(
            model_name,
            train_y,
            train_x,
            test_y,
            pred,
            model,
        )

    def elasticnet(
        self,
        model_name,
        train_x,
        test_x,
        train_y,
        test_y,
    ):
        model = linear_model.ElasticNet(alpha=1)
        model.fit(train_x, train_y)
        pred = model.predict(test_x)
        self.print_score(
            model_name,
            train_y,
            train_x,
            test_y,
            pred,
            model,
        )

    def print_score(
        self,
        model_name,
        train_y,
        train_x,
        test_y,
        pred,
        model,
    ):
        try:
            print ('Mean squared error' + model_name + ' : ',
                   mean_squared_error(test_y, pred))
            print ('R squared:  ' + model_name + ' : ',
                   r2_score(test_y, pred))
        except Exception:
            traceback.print_exc()

if __name__ == '__main__':
    obj = Compute()
    (train_x, test_x, train_y, test_y) = obj.data_loader()
    models = [
            "svr",
            "lasso",
            "elasticnet",
            "ridge",
            "linear",
            "polynomial",
            ]
    for i in models:
        obj2=Algorithms(i,train_x, test_x, train_y, test_y)
