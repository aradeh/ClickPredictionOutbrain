import math
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LogisticRegression, LinearRegression

tr_data = pd.read_csv('clicks_train.csv')




X = []
for m,n in zip(tr_data['display_id'],tr_data['ad_id']):
        ids = []
        ids.append(m)
        ids.append(n)
        X.append(ids)

X= np.array(X)
y= np.array(tr_data['clicked'])

#X= X.reshape(X)
#y=y.reshape(y)
X = preprocessing.scale(X)
#X = X[:1]
#tr_data.dropna(inplace=True)

#y = np.array(tr_data['clicked'])

print(len(X),len(y))

#X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y, test_size=0.2)

classifier = LogisticRegression()
classifier.fit(X,y)


tst_data = pd.read_csv('clicks_test.csv')
X_test = []
for m,n in zip(tst_data['display_id'],tst_data['ad_id']):
        ids = []
        ids.append(m)
        ids.append(n)
        X_test.append(ids)

X_test = np.array(X_test)

acc = classifier.score(X_test,y)

print(acc)