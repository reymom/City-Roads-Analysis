import networkx as nx
import osmnx as ox
import numpy as np
import random

from time import time

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

from histogramaker import hist
from road_functions import cumulative, distancia_euclidea, efficiency

#Z = ox.graph_from_point((41.6173,0.6164),distance=2000,network_type='drive')
#Z = ox.graph_from_place('Lleida, Spain',network_type='drive')

#Z = ox.graph_from_point((41.37848,2.17364),distance=2000,network_type='drive')
#Z = ox.graph_from_place('Barcelona, Spain',network_type='drive')

Z = ox.graph_from_place('Palma de Mallorca, Spain',network_type='drive')

G_proj = ox.project_graph(Z)
ox.plot_graph(G_proj,bgcolor='#000000',node_size=0,node_color="black",edge_color="#ffffff",edge_linewidth=0.4,edge_alpha=0.3)
G = nx.convert_node_labels_to_integers(Z)
N = len(G.nodes())
###Difussivity coeficient for random trajectories
#mira nodo central,donde enchufaras coches

center_point = (41.6173, 0.6164)
center_node = ox.get_nearest_node(G, center_point, return_dist=True)
print(center_node)

position_counter=[]
for n in range(N):
    position_counter.append(0)
    
G = G.to_undirected()

movimientos=10000
actual_node=center_node
for t in range(movimientos):
    node_options = list(G.edges(actual_node))
    print(node_options)
    posibilidades=len(node_options)
    next_node=random.randint(0,posibilidades-1)
    actual_node=node_options[next_node][1]
    position_counter[actual_node]=position_counter[actual_node]+1
    
print(position_counter)
print("ultimo nodo el ",actual_node)

prob_distancias=[]
for i in range(N):
    None
    