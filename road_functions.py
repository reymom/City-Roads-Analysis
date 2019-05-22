import networkx as nx
import osmnx as ox
import numpy as np
from time import time

def cumulative(probs):
    cumul = []
    cum = 0.
    for i in range(len(probs)):
        cum=cum+probs[-(i+1)]
        cumul.append(cum)
    cumul = cumul[::-1]
    return cumul

def distancia_euclidea(lat1,long1,lat2,long2):
    lat1=lat1*np.pi/180.
    lat2=lat2*np.pi/180.
    long1=long1*np.pi/180.
    long2=long2*np.pi/180.
    R=6371000.
    return abs(np.arccos(np.sin(lat1)*np.sin(lat2)+np.cos(lat1)*np.cos(lat2)*np.cos(long2-long1))*R)

def efficiency(H):
    Num = len(H.nodes())
    dij= dict(nx.shortest_path_length(H))
    sumaij=0.
    for i in range(Num+1):
        if i in list(H.nodes()):
            for j in range(Num+1):
                if j in list(H.nodes()):
                    if i != j:
                        try:
                            if dij[i][j] > 0:
                                lat1=H.nodes()[i]['y']
                                long1=H.nodes()[i]['x']
                                lat2=H.nodes()[j]['y']
                                long2=H.nodes()[j]['x']
                                sumaij += distancia_euclidea(lat1,long1,lat2,long2)/float(dij[i][j])
                        except:
                            #print("%i-%i no reachable"%(i,j))
                            continue
    EH=sumaij/(Num*(Num+1))
    return EH