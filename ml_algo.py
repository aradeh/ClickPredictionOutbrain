import csv
from scipy import sparse
import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors

dt = pd.read_csv('clicks_test.csv')
df = pd.read_csv('clicks_train.csv')

#print(df.head())

feature = np.array(df['display_id'],df['ad_id'])
c_class = np.array(df['clicked'])

mlc = neighbors.KNeighborsClassifier()
mlc.fit(feature,c_class)

c_test = np.array(dt['display_id'],dt['ad_id'])
p_test = np.array(dt['ad_id'])

acc = mlc.score(c_test,p_test)
print(acc)
