from collections import Counter
class KNN:
    def __init__(self,n_neighbors):
        self.n_neighbors = n_neighbors
    def fit(self,X,y):
        self.X_train = X
        self.y_train = y
    def predict(self,X_test):
        self.X_test = X_test
        distance = []
        index = 1
        for i in self.X_train:
            dis = ((self.X_test[0][0] - i[0]) ** 2 + (self.X_test[0][1] - i[1])**2)**0.5
            distance.append([index,dis])
            index+=1
        distance = sorted(distance,reverse=True)
        # print(distance)
        return self.classify(distance[:self.n_neighbors])
    def classify(self,distance):
        label = []
        for i in distance:
            label.append(self.y_train[i[0]-1])
        freq =  Counter(label)
        pred = freq.most_common(1)[0][0]
        print(freq)
        print("Most Common [1] : " ,freq.most_common(1)[0][0])
        print("Prediction : ", pred)
        return "KNN Closed"
    