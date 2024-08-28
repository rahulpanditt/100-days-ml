import random
import numpy as np


class Kmeans:
    def __init__(self, n_cluster=2, max_iter=100):
        self.n_cluster = n_cluster
        self.max_iter = max_iter

    def fit_predict(self, X):
        random_index = (random.sample(range(0, X.shape[0]), self.n_cluster))
        self.centroid = X[random_index]
        for i in range(self.max_iter):
            # assign cluster
            cluster_group = self.assign_clusters(X)
            # move centroid 
            old_centroid = self.centroid
            self.centroid = self.move_centroid(X,cluster_group)
        #  check finish (prev and new centroid same or not)
            if np.allclose(old_centroid, self.centroid):
                break

        print(cluster_group)
        return cluster_group

    def assign_clusters(self, X):
        cluster_group = []
        distance = []
        for row in X:
            for centroid in self.centroid:
                distance.append(np.sqrt(np.dot((row-centroid), (row-centroid))))
            min_distance = min(distance)
            index_pos = distance.index(min_distance)
            cluster_group.append(index_pos)
            distance.clear()
        return np.array(cluster_group)
    def move_centroid(self,X,cluster_group):
        new_centroid = []
        cluster_type = (np.unique(cluster_group))
        for type in cluster_type:
            new_centroid.append(X[cluster_group==type].mean(axis=0))
        return new_centroid