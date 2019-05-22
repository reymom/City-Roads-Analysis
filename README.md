# City-Roads-Analysis
Some programs in order to play a little bit with the libraries of OSMnx and NetworkX

## Content
road_functions.py: cumulative distribution, euclidean distance and efficiency (interesting kind of centrality measure that tells us what the impact of removing some road would be for the overall traffic)

road_mallorca.py: analysis of certain traits of Palma de Mallorca

road_osmnx.py: to extract networks and just see few things (dirty)

zombie_walk.py: creative project not finished, the idea is to put some dynamics in the network representing the traffic of cars in certain situation that could be a zombie catastrophe

## Insights

Comparing the simple results I obtained doing some calculus, I realized that Lleida has its centrality distribution as in a self-organized city (see paper, results of Ahmedabad and El Cairo) which firms that it follows a power law distribution. For Palma it is not directly observable this fact, but I could guess it is to some extend self-organized but with some structural planning (for totally planned cities we have an exponential distribution for the) in some moments of its history. In fact, if I do the analysis for the center I get the power law for the C_I, so it seems (it is also intuitive) 
that the center grew up in a self-organized way but then in more modern era there was to some extend some urbanistic plan.
I did also some simulations running some biased random-walker dynamics, trying to play and imagine the results 
of a zombie burst in the center, in such a way that the flow of cars has the tendency to scape from the point of the burst 
(go outside the city), but in the confusion and panic of the moment they also have a component of wandering in some erratic way. 
I watched for the distance distribution of nodes where the cars arrived at some point, but I didn't make to calculate the diffusion. 
I could have done a more subtle game as considering finite time, inside the time steps between iterations, between moves among nodes (in function of the Euclidian distance) and some rules for traffic, for example simulating crashes when more than $n$ cars collide in some node, then cutting its links from the network. Then it would be more interesting to see the difussion coefficient, doing averages for several simulations, for the different networks of the different cities in order to see on which one I would prefer to live if we were near an imminent apocalypse.

## References
P. Crucitti, V. Latora and S. Porta. (2006). Centrality measures in spatial networks of urban streets. *PHYSICAL REVIEW E 73, 036125. DOI: 10.1103/PhysRevE.73.036125
