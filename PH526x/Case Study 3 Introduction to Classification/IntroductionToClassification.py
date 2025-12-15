import numpy as np
import random
import scipy.stats as ss


def distance(p1, p2):
    return np.sqrt(sum(np.power(p2 - p1, 2)))


def majority_vote(votes):
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


def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode


# p1 = np.array([1, 1])
# p2 = np.array([4, 4])
# print(distance(p1, p2))
votes = [1, 2, 3, 1, 2, 3, 3, 3, 3]
print(majority_vote(votes))
print(majority_vote_fast(votes))
