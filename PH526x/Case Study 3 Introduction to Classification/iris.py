# Iris dataset

import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt
from plot_prediction_grid import plot_prediction_grid
from sklearn.datasets import load_iris


# Majority vote
def majority_vote(votes):
    """docs string"""
    vote_counts = {}
    for vote in votes:
        if vote not in vote_counts:
            vote_counts[vote] = 1
        else:
            vote_counts[vote] += 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners)


def distance(p1, p2):
    """Find the distance between 2 points p1 and p2."""
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


# find nearest neighbors function


def find_nearest_neighbors(p, points, k=5):
    """Find the k nearest neighbors of point p and return their indices."""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


# predict function


def knn_predict(p, points, outcomes, k=5):
    # find k nearest neighbors
    ind = find_nearest_neighbors(p, points, k)
    # predict the class of p based on majority vote
    return majority_vote(outcomes[ind])


# print(knn_predict(p, points, outcomes, k=2))


# synthetic data
def generate_synth_data(n=50):
    """Creat two sets of points from bivariate normal distributions."""
    points = np.concatenate(
        (ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis=0
    )
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)


# Prediction grid
def make_prediction_grid(predictors, outcomes, limits, h, k):
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_gird = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_gird[j, i] = knn_predict(p, predictors, outcomes, k)

    return (xx, yy, prediction_gird)


# Plot prediction grid
'''
def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
'''

iris = load_iris()
print(iris.keys())

predictors = iris["data"][:, 0:2]
outcomes = iris["target"]

plt.plot(predictors[outcomes == 0][:, 0], predictors[outcomes == 0][:, 1], "ro")
plt.plot(predictors[outcomes == 1][:, 0], predictors[outcomes == 1][:, 1], "go")
plt.plot(predictors[outcomes == 2][:, 0], predictors[outcomes == 2][:, 1], "bo")
plt.show()


k = 5
filename = "iris_grid.pdf"
limits = (4, 8, 1.5, 4.5)
h = 0.1

(xx, yy, prediction_gird) = make_prediction_grid(predictors, outcomes, limits, h, k)

plot_prediction_grid(xx, yy, prediction_gird, filename)
