#ignore
from knnPrac import KNN
import pandas as pd # type: ignore
import numpy as np #type:ignore
from knn import KNearestNeighbors
data = pd.read_csv("Social_Network_Ads.csv")
X = data.iloc[:,2:4].values
y = data.iloc[:,-1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# print(X_train)bn
# an object of KNN Class
# knn = KNearestNeighbors(4)
# knn.fit(X_train,y_train)
# knn.predict(np.array([60,100]).reshape(1,2))
# an object of KNNPrac Class
KNN = KNN(5)
KNN.fit(X_train,y_train)
print(KNN.predict(np.array([60,100]).reshape(1,2)))