import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('cpm_data.csv')

# Create a directed graph using networkx
G = nx.DiGraph()

# Add nodes and edges to the graph
for index, row in df.iterrows():
    G.add_edge(row['start_node'], row['end_node'], weight=row['duration'])

# Calculate the earliest start time (EST) and earliest finish time (EFT)
est = {node: 0 for node in G.nodes}
eft = {node: 0 for node in G.nodes}

for node in nx.topological_sort(G):
    est[node] = max([eft[predecessor] for predecessor in G.predecessors(node)], default=0)
    eft[node] = est[node] + max([G[predecessor][node]['weight'] for predecessor in G.predecessors(node)], default=0)
    print(eft[node])
# Calculate the latest start time (LST) and latest finish time (LFT)
lst = {node: eft[G.nodes[node]['start_node']] for node in G.nodes}
lft = {node: lst[node] + G.nodes[node]['duration'] for node in G.nodes}

# Calculate slack for each activity
slack = {edge: lst[edge[1]] - eft[edge[0]] for edge in G.edges}

# Identify the critical path
critical_path_edges = [edge for edge in G.edges if slack[edge] == 0]

# Print results
print("EST:", est)
print("EFT:", eft)
print("LST:", lst)
print("LFT:", lft)
print("Slack:", slack)
print("Critical Path Edges:", critical_path_edges)

# Draw the network diagram
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=critical_path_edges, edge_color='r', width=2)
plt.show()
