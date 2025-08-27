"""
Important Note
Most Python distributions available in 2018 and later include version 2.0 or higher of NetworkX. Version 2.0 of NetworkX introduced several significant changes. This version and higher versions behave differently from previous versions in certain areas.

For this video...

Note that G.degree() now returns a DegreeView object rather than a dictionary.
In the video at about 4:07, we used the following line of code:
print("Average degree: %.2f" % np.mean(list(G.degree().values)))
The above line must be replaced with the following lines of code:

degree_sequence = [d for n, d in G.degree()]
print("Average degree: %.2f" % np.mean(degree_sequence))
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

cwd = os.path.dirname(os.path.abspath(__file__))
# Change to the directory where the script is located
os.chdir(cwd)
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

# convert the adjacency matrices to graph objects
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

print(G1.number_of_nodes(), G2.number_of_nodes())
print(G1.number_of_edges(), G2.number_of_edges())


def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of nodes: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))


def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")


basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.show()
