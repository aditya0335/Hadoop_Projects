import sys
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
list_features=[]
list_labels=[]
# Importing test file from pandas
test_sample=pd.read_csv('Test.csv')
test_sample=np.asarray(test_sample)
# test_sample=test_sample[:,0:48]

# Reading trian data line by line
for line in sys.stdin:
    data=line.strip( )
    data=line.split(",")
    list_features.append(data[0:48])
    list_labels.append(data[48])
# print(list)

list_features=pd.DataFrame(list_features)
list_features=list_features.to_numpy()
list_features=np.array(list_features,dtype=np.float)
list_labels=pd.DataFrame(list_labels)
list_labels=list_labels.to_numpy()
list_labels=np.array(list_labels,dtype=np.int)
scaler = MinMaxScaler()
features_train=scaler.fit_transform(list_features)
features_test=scaler.transform(test_sample)
i=0
for row in features_test:
    row=row.reshape(1,np.size(list_features,1))
    distance=np.sqrt(np.sum(np.square((np.subtract(np.repeat(row,np.size(list_features,0),0),features_train))),axis=1))
    row_name=np.repeat(i,np.size(list_features,0),0)
    row_name=row_name.reshape(np.size(list_features,0),1)
    distance = distance.reshape(np.size(list_features,0), 1)
    list_labels = list_labels.reshape(np.size(list_features,0), 1)
    distance = np.concatenate((row_name[1:],distance[1:],list_labels[1:]), axis=1)
    i += 1
    for dist in distance:
        print('%i\t%f\t%i'%(dist[0],dist[1],dist[2]))

