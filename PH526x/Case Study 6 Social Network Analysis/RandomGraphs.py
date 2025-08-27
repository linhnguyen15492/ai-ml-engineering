import networkx as nx
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np


def er_graph(N, p):
    """Generate an ER graph"""
    G = nx.Graph()  # create empty graph
    G.add_nodes_from(range(N))  # add all N nodes in the graph
    for node1 in G.nodes():  # so loop over all pairs of nodes
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p):  # add an edge with prob p
                G.add_edge(node1, node2)
    return G


def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    # plt.show()


# N = 50
# p = 0.08
# nx.draw(er_graph(N, p), node_size=40)
# G = er_graph(N, p)
# plt.show()

G1 = er_graph(500, 0.08)
plt.figure(figsize=(8, 6))
plot_degree_distribution(G1)

G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)

G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.show()


# G4 = nx.erdos_renyi_graph(10, 0)
# nx.draw(G4, node_size=40, node_color="green")
# plt.title("Erdős-Rényi Graph with N=10, p=0")
# plt.show()
