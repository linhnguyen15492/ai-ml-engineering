import numpy as np
import matplotlib.pyplot as plt
import random
import scipy.stats as ss


def distance(p1, p2):
    """Find the distance between points p1 and p2."""
    return np.sqrt(sum(np.power(p2 - p1, 2)))


def majority_vote(votes):
    """Return the most commom element in votes."""
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1

    winner = []
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            winner.append(vote)
    return random.choice(winner)


def majority_vote_short(votes):
    """Return the most commom element in votes, short version using scipy library."""
    mode, count = ss.mtstats.mode(votes)
    return mode


def find_nearest_neighbors(p, points, k=5):
    """Find the k neareast neighbors of point p and return their indices."""
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)  # get the indices of distances
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])


def generate_synth_data(n=50):
    """Create two sets of points from bivariate normal distributions."""
    points = np.concatenate(
        (ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis=0
    )
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)


n = 20
(points, outcomes) = generate_synth_data(n)
# print(knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2))

plt.Figure()
plt.plot(points[:n, 0], points[:n, 1], "ro")
plt.plot(points[n:, 0], points[n:, 1], "bo")
