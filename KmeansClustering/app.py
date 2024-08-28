from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from kmeansPrac import Kmeans
centroids =  [(-5,-5),(5,5)] 
clusters_std = [1,1]
X,y = make_blobs(n_samples=100,cluster_std=clusters_std,centers=centroids,n_features=2,random_state=2)
km = Kmeans(n_cluster=2,max_iter=100)
y_means  = km.fit_predict(X)
plt.scatter(X[y_means == 0, 0], X[y_means  == 0, 1], c='red', label='Cluster 1')
plt.scatter(X[y_means == 1, 0], X[y_means == 1, 1], c='blue', label='Cluster 2')
print(y)
print(km.centroid)
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()