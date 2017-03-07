import pandas as pd
import numpy as np
import math

tr_data = pd.read_csv('clicks_train.csv',nrows=21785433)

#train_df = pd.concat(tr_data,ignore_index=True)

print(len(tr_data))

positive_vectors = []
negative_vectors = []

#for i in tr_data:
#    print i


for m,n,i in zip(tr_data['display_id'],tr_data['ad_id'],tr_data['clicked']):
    if i == 1:
        ids = []
        ids.append(m)
        ids.append(n)
        positive_vectors.append(ids)
    else:
        nids = []
        nids.append(m)
        nids.append(n)
        negative_vectors.append(nids)

#print(negative_vectors)


train_data_dict = {-1: np.array(negative_vectors),
                   1: np.array(positive_vectors)
                   }

print(train_data_dict)