import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

GRAPH_TYPE = "Undirected Unweighted Graph"
filename = f"GraphTheory_ShortestPathProblems/Visualizations/assets/{GRAPH_TYPE.replace(' ', '_')}.png"
# add graph
graph = [
    [0, 1, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
]
G = nx.Graph()

# add nodes
for i in range(len(graph)):
    G.add_node(i)

# add edges
for i, row in enumerate(graph):
    for j, value in enumerate(row):
        if i < j and value == 1:
            G.add_edge(i, j)

pos = nx.spring_layout(G)

# draw graph
plt.figure(figsize=(8, 8))
nx.draw_networkx(
    G,
    pos,
    with_labels=True,
    node_size=500,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
)

path = nx.shortest_path(G, source=0, target=9)
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="r")
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="r", width=2)

legend_elements = [Line2D([0], [0], color="red", lw=4, label="Shortest Path")]
plt.legend(handles=legend_elements, loc="upper right")

plt.title("Unweighted Undirected Graph")
plt.savefig(filename)
plt.show()
