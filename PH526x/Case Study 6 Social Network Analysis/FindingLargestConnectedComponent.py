import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)
A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")

# convert the adjacency matrices to graph objects
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)


def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")


def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of nodes: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))


subgraph_1 = (G1.subgraph(c) for c in nx.connected_components(G1))
subgraph_2 = (G2.subgraph(c) for c in nx.connected_components(G2))
LCC_1 = max((G1.subgraph(c) for c in nx.connected_components(G1)), key=len)
LCC_2 = max((G2.subgraph(c) for c in nx.connected_components(G2)), key=len)

plt.figure()
nx.draw(LCC_1, node_color="red", edge_color="gray", node_size=20)
plt.title("Largest Connected Component of G1")
plt.show()

plt.figure()
nx.draw(LCC_2, node_color="green", edge_color="gray", node_size=20)
plt.title("Largest Connected Component of G2")
plt.show()

# for sub in list(subgraph_1):
#     plt.figure()
#     nx.draw(sub, node_color='blue', node_size=20)


for i, sg in enumerate(subgraph_1):
    print("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
    print("\tNodes:", sg.nodes(data=True))  # có thể lược bỏ data=True
    print("\tEdges:", sg.edges())


# for i, sg in enumerate(subgraph_2):
#     print("subgraph {} has {} nodes".format(i, sg.number_of_nodes()))
#     print("\tNodes:", sg.nodes(data=True))  # có thể lược bỏ data=True
#     print("\tEdges:", sg.edges())
