import networkx as nx
import matplotlib.pyplot as plt


G = nx.karate_club_graph()

print(G.number_of_nodes(), G.number_of_edges())
print("Nodes:", G.nodes())
print("Edges:", G.edges())
print("Node degrees:", G.degree())

nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.title("Karate Club Graph")
plt.show()
