import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# from plot_prediction_grid import plot_prediction_grid
# from classification_final import make_prediction_grid
from classification_final import knn_predict

iris = load_iris()
print("Load Iris completed")

predictors = iris.data[:, 0:2]
outcomes = iris.target
print("Create predictors and outcomes")

"""
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], 'ro')
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], 'go')
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], 'bo')
plt.show()
print('Plot completed')


k=5; filename='iris_gird.pdf'; limits=(4,8,1.5,4.5); h=0.1

(xx, yy, prediction_gird) = make_prediction_grid(predictors, outcomes, limits, h, k)

plot_prediction_grid(xx, yy, prediction_gird, filename, predictors, outcomes) """

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

# print(sk_prediction.shape)
my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])

percentage = np.mean(sk_predictions == my_predictions) * 100
print("sk vs my predictions")
print(percentage)
print("sk predictions vs outcomes")
print(np.mean(sk_predictions == outcomes) * 100)
print("my predictions vs outcomes")
print(np.mean(my_predictions == outcomes) * 100)
