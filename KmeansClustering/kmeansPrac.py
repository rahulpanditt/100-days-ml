import random
import numpy as np
class Kmeans:
    def __init__(self,n_cluster=2,max_iter=100) -> None:
        self.n_cluster = n_cluster
        self.max_iter = max_iter
    
    def fit_predict(self,X):
        random_index = random.sample(range(0,X.shape[0]),k=self.n_cluster)
        self.centroid = X[random_index]
        print("Centroid :  " , self.centroid)
        for i in range(self.max_iter):
            cluster_group = self.cluster_group(X,self.centroid)
            old_centroid = self.centroid
            self.centroid = self.moveCentroid(X,cluster_group)
            if np.allclose(old_centroid,self.centroid):
                break
        return cluster_group
    def cluster_group(self,X,centroids):
        cluster_group = []
        distance = []
        for row in X:
            for centroid in centroids:
                distance.append(np.sqrt(np.dot((row-centroid),(row-centroid))))
            min_distance = min(distance)
            min_index = distance.index(min_distance)
            # print(min_index)
            distance.clear()
            cluster_group.append(min_index)
        return np.array(cluster_group)
    def moveCentroid(self,X,cluster_group):
        centroid = []
        types = np.unique(cluster_group)
        for type in types:
            centroid.append(np.mean(X[cluster_group==type]))
        print(cluster_group)
        return centroid