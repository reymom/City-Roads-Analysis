import networkx as nx
import osmnx as ox
import numpy as np
import requests
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
from histogramaker import hist
from time import time
from road_functions import cumulative, distancia_euclidea, efficiency

###.............................##
###...........EXCTRACT_MAPS.....##
###.............................##

#G = ox.graph_from_place('Palma de Mallorca, Spain',network_type='drive') #toda mallorca
t0=time()
Z = ox.graph_from_point((39.5713,2.6490),distance=500,network_type='drive') #reducida


#G = G.to_undirected()

#G = ox.graph_from_place('Lleida, Spain',network_type='drive')
#Z = ox.graph_from_point((41.6173,0.6164),distance=750,network_type='drive') #
#print(Z.nodes())
G = nx.convert_node_labels_to_integers(Z)
#print(G.nodes())
#print(G.edges())

"""
for i in G.nodes():
    print("NODE %i"%i)
    print(G.nodes()[i]['x'], G.nodes()[i]['y'])
"""
    

#G = ox.graph_from_place('Zaidin, Spain',network_type='drive')
#G = ox.graph_from_point((41.6052,0.2657),distance=1000,network_type='drive'))

#G = ox.graph_from_place('Benasque, Spain',network_type='drive')

###........................##
###.........GRAFICAR LA RED##
###........................##
t0=time()
ox.plot_graph(G,node_size=5,node_color="black",edge_color="blue",edge_linewidth=0.4,edge_alpha=0.3)
#print("%.2f seg para graficarla" %(time()-t0))
###........................##
###.....FEW CHARACTERISTICS##
###........................##

#G_proj = ox.project_graph(G)
#nods = ox.graph_to_gdfs(G, nodes=True, edges=False)
#print(nods.columns[1])
#for i in nods.geometry:
    #print(i)

#UTIL#
#stats = ox.basic_stats(graph_proj)
N=len(G.nodes())
L=len(G.edges())
print("N = ", N)
print("L = ", L)

###........................##
###........NETWORKS_CHARACT##
###........................##

#node_centrality = nx.closeness_centrality(G)
#n_c = list(node_centrality.values())
#n_cs,p_nc,er=hist(n_c,30)

t0 = time()
betw_centrality = nx.betweenness_centrality(G)
#print(r"%.5f seg para calcular $B_c$ con nx" %(time()-t0))
b_c = list(betw_centrality.values())
bcs,pbc,er=hist(b_c,25)

###MAKING CUMULATIVE###
pbc_cumul = cumulative(pbc)


###STRAIGHTNESS CENTRALITY###
###INFORMATION CENTRALITY###
#E es la eficiencia, Gprima la red sin el nodo i (y sin sus edges, obiamente)
#CI_i = (EG-EGprima)/EGprima


t0 = time()
EG=efficiency(G)
print("%.5f seg para calculo E(G)" %(time()-t0))
print(r"$E_G$=",EG)
print("comienza CI")
print("-----------")
print(" ")
CI=[]
t0=time()
for i in range(N):
    if (G.in_degree(i)>1 and G.out_degree(i)>1):
        I = G.copy()
        I.remove_node(i)
        Gprima = I.copy()
        tini=time()
        EGprima=efficiency(Gprima)
        tfin=time()
        CI.append((EG-EGprima)/EG)
        print("CI_%i=%.5f" % (i,CI[-1]))
        print("tiempo=%.4f"%(time()-t0))
        print(".........")

#print(r"%.5f seg para calculo todos $C_I$" %(time()-t0))
ci,pci,er=hist(CI,25)
pci_cum = cumulative(pci)

"""
plt.figure(1)
plt.xlabel(r"$C^C$")
plt.ylabel(r"$P(C^C)$")
plt.plot(n_cs,p_nc)
plt.show()
"""

plt.figure(1)
plt.title("Betweennes centrality cumulative distribution")
plt.yscale('log')
plt.xlabel(r"$C^B$")
plt.ylabel(r"$P(C^B)$")
plt.plot(bcs,pbc_cumul,'.')
plt.show()

plt.figure(2)
plt.title("cumulative CI")
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r"$C^I$")
plt.ylabel(r"$P(C^I)$")
plt.plot(ci,pci_cum,'.')
plt.show()

plt.figure(2)
plt.title("cumulative CI")
plt.xlabel(r"$C^I$")
plt.ylabel(r"$P(C^I)$")
plt.plot(ci,pci_cum,'.')
plt.show()
plt.figure(2)
plt.title("cumulative CI")
plt.yscale('log')
plt.xlabel(r"$C^I$")
plt.ylabel(r"$P(C^I)$")
plt.plot(ci,pci_cum,'.')
plt.show()