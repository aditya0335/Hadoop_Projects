import sys
import os
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
distance_sort=[]
test_sample=pd.read_csv('Test.csv')
test_sample=np.asarray(test_sample)
k_value=50
for line in sys.stdin:
    line = line.strip( )
    distance = line.split("\t")
    distance_sort.append(distance)
distance_sort=pd.DataFrame(distance_sort)
distance_sort=distance_sort.to_numpy()
distance_sort=np.array(distance_sort,dtype=np.float)
matrix=np.array((np.split(distance_sort, np.where(np.diff(distance_sort[:,0]))[0]+1)))
testing=[]
for tile in matrix:
    tile = tile[np.argsort(tile[:, 1])]
    tile=tile[:k_value,]
    test_row=int(tile[0,0])
    knn=tile[:,2]
    knn=knn.astype(int)
    result=np.bincount(knn).argmax()
    print('%i,%s,%i'%(test_row,test_sample[test_row,:],result))

