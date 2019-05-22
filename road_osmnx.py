import networkx as nx
import osmnx as ox
import requests
import matplotlib.cm as cm
import matplotlib.colors as colors


#G = ox.graph_from_place('Zaidin, Spain',network_type='drive')

#G = ox.graph_from_place('Lleida, Spain',network_type='drive')

#G = ox.graph_from_place('Palma de Mallorca, Spain',network_type='drive')

#G = ox.graph_from_place('Benasque, Spain',network_type='walk')
#G = ox.graph_from_point((39.5713,2.6490),distance=500,network_type='drive')
G = ox.graph_from_point((41.6052,0.2657),distance=1000,network_type='drive')

ox.plot_graph(G,node_size=10,node_color="black",edge_color="blue",edge_linewidth=0.6,edge_alpha=1)
#G_proj = ox.project_graph(G)
#nodes_proj = ox.graph_to_gdfs(G_proj, edges=False)
#graph_area_m = nodes_proj.unary_union.convex_hull.area
#print(ox.basic_stats(G_proj, area=graph_area_m, clean_intersects=True, circuity_dist='euclidean'))
"""
G = G.to_undirected()
grados= G.degree()
indigrad = [i[1] for i in G.degree()]
print(indigrad)
print(len(grados))
print(len(G.nodes()))
print(float(sum(indigrad))/len(grados))
#print(r"$<k_in>=$",sum( [i for (i,j) in G.in_degree()] ) /len(G.nodes()))
#print(r"$<k_out>=$",sum([[i[1] for i in G.out_degree()])/len(G.nodes()))
"""
# edge closeness centrality: convert graph to line graph so edges become nodes and vice versa
edge_centrality = nx.closeness_centrality(nx.line_graph(G))


# list of edge values for the orginal graph
ev = [edge_centrality[edge + (0,)] for edge in G.edges()]

# color scale converted to list of colors for graph edges
norm = colors.Normalize(vmin=min(ev)*0.8, vmax=max(ev))
cmap = cm.ScalarMappable(norm=norm, cmap=cm.inferno)
ec = [cmap.to_rgba(cl) for cl in ev]

# color the edges in the original graph with closeness centralities in the line graph
fig, ax = ox.plot_graph(G, bgcolor='k', axis_off=True, node_size=0, edge_color=ec, edge_linewidth=1.5, edge_alpha=1)

